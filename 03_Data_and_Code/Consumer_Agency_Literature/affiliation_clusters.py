"""Cluster universities by shared-paper affiliations and overlay reviewed mechanisms."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
import numpy as np
import pandas as pd
import networkx as nx
from sklearn.metrics import adjusted_rand_score
from cluster import FEATURES, RISK

HERE = Path(__file__).resolve().parent


def make_graph(pairs, fractional=True):
    graph = nx.Graph()
    graph.add_nodes_from(sorted(pairs.institution_id.unique()))
    multipaper = 0
    for _, group in pairs.groupby('paper_id', sort=True):
        nodes = sorted(set(group.institution_id))
        k = len(nodes)
        if k < 2:
            continue
        multipaper += 1
        weight = 2 / (k * (k - 1)) if fractional else 1.0
        for left, right in combinations(nodes, 2):
            if not graph.has_edge(left, right):
                graph.add_edge(left, right, weight=0.0, shared_papers=0)
            graph[left][right]['weight'] += weight
            graph[left][right]['shared_papers'] += 1
    if fractional:
        assert np.isclose(graph.size(weight='weight'), multipaper)
    assert nx.number_of_selfloops(graph) == 0
    return graph


def communities(graph, seed=534, resolution=1):
    connected = graph.subgraph([n for n in graph if graph.degree(n) > 0]).copy()
    groups = nx.community.louvain_communities(connected, weight='weight', seed=seed, resolution=resolution)
    return connected, groups


def labels(groups, nodes):
    lookup = {node: i for i, group in enumerate(groups) for node in group}
    return [lookup[node] for node in nodes]


def main():
    pairs = pd.read_csv(HERE / 'paper_affiliations.csv').sort_values(['paper_id', 'institution_id'])
    coverage = pd.read_csv(HERE / 'affiliation_coverage.csv')
    reviews = pd.read_csv(HERE / 'coded_papers.csv')
    assert not pairs.duplicated(['paper_id', 'institution_id']).any()
    assert coverage.paper_id.is_unique and reviews.id.is_unique
    pairs['paper_weight'] = 1 / pairs.groupby('paper_id').institution_id.transform('size')
    np.testing.assert_allclose(pairs.groupby('paper_id').paper_weight.sum(), 1)
    graph = make_graph(pairs)
    connected, groups = communities(graph)
    # Community IDs are display labels ordered by fractional publication mass.
    mass = pairs.groupby('institution_id').paper_weight.sum()
    groups = sorted(groups, key=lambda g: (-float(mass.loc[list(g)].sum()), min(g)))
    membership = {node: f'C{i+1:02d}' for i, group in enumerate(groups) for node in group}
    pairs['community'] = pairs.institution_id.map(membership).fillna('Unconnected')
    universities = pairs.groupby(['institution_id', 'institution_name', 'community']).agg(
        papers=('paper_id', 'nunique'), fractional_papers=('paper_weight', 'sum')).reset_index()
    universities['weighted_degree'] = universities.institution_id.map(dict(graph.degree(weight='weight')))
    # Split each paper across its universities; its total contribution remains one.
    allocation = pairs.groupby(['paper_id', 'community']).paper_weight.sum().reset_index()
    allocation = allocation.merge(coverage, on='paper_id', validate='many_to_one')
    allocation = allocation.merge(reviews[['id'] + FEATURES], left_on='paper_id', right_on='id',
                                  how='left', validate='many_to_one').drop(columns='id')
    output = HERE / 'results/affiliations'
    output.mkdir(parents=True, exist_ok=True)
    university_rows, mechanism_rows = [], []
    for community, group in allocation.groupby('community', sort=True):
        members = universities.loc[universities.community == community].sort_values(
            ['fractional_papers', 'institution_name'], ascending=[False, True])
        reviewed = group.loc[group.review_status.ne('not_reviewed')]
        risk = group.loc[group.review_status.isin(RISK)]
        assert not risk[FEATURES].isna().any().any()
        university_rows.append({'community': community, 'universities': len(members),
            'distinct_papers': group.paper_id.nunique(), 'fractional_papers': group.paper_weight.sum(),
            'reviewed_papers': reviewed.paper_id.nunique(), 'reviewed_fractional_papers': reviewed.paper_weight.sum(),
            'risk_reviewed_papers': risk.paper_id.nunique(), 'risk_reviewed_fractional_papers': risk.paper_weight.sum(),
            'largest_affiliations_by_fractional_papers': '; '.join(members.institution_name.head(4))})
        for feature in FEATURES:
            numerator = (risk[feature] * risk.paper_weight).sum()
            denominator = risk.paper_weight.sum()
            mechanism_rows.append({'community': community, 'feature': feature,
                'weighted_positive': numerator, 'weighted_reviewed_risk_denominator': denominator,
                'share': numerator / denominator if denominator else None,
                'distinct_reviewed_risk_papers': risk.paper_id.nunique(),
                'small_review_sample': risk.paper_id.nunique() < 10})
    nodes = sorted(connected)
    reference = labels(groups, nodes)
    sensitivity = []
    for resolution in [.5, 1., 1.5]:
        for seed in range(20):
            _, candidate = communities(graph, seed=seed, resolution=resolution)
            sensitivity.append({'resolution': resolution, 'seed': seed, 'communities': len(candidate),
                'modularity': nx.community.modularity(connected, candidate, weight='weight', resolution=resolution),
                'ari_against_primary': adjusted_rand_score(reference, labels(candidate, nodes))})
    full_graph = make_graph(pairs, fractional=False)
    _, full_groups = communities(full_graph)
    edges = [{'left': a, 'right': b, **d} for a, b, d in graph.edges(data=True)]
    university_table = pd.DataFrame(university_rows)
    assert np.isclose(university_table.fractional_papers.sum(), pairs.paper_id.nunique())
    universities.to_csv(output / 'university_membership.csv', index=False)
    university_table.to_csv(output / 'community_summary.csv', index=False)
    allocation.to_csv(output / 'paper_community_weights.csv', index=False)
    pd.DataFrame(mechanism_rows).to_csv(output / 'mechanism_profiles.csv', index=False)
    pd.DataFrame(edges).to_csv(output / 'university_edges.csv', index=False)
    sensitivity = pd.DataFrame(sensitivity)
    sensitivity.to_csv(output / 'sensitivity.csv', index=False)
    journal = allocation.groupby(['community', 'journal']).paper_weight.sum().reset_index()
    journal.to_csv(output / 'journal_profiles.csv', index=False)
    same_resolution = sensitivity.loc[sensitivity.resolution.eq(1), 'ari_against_primary']
    summary = {'eligible_papers': len(coverage), 'papers_with_university': pairs.paper_id.nunique(),
        'papers_without_university': int(coverage.university_count.eq(0).sum()),
        'multi_university_papers': int(coverage.university_count.gt(1).sum()),
        'universities': graph.number_of_nodes(), 'edges': graph.number_of_edges(),
        'unconnected_universities': len(list(nx.isolates(graph))), 'communities': len(groups),
        'connected_components': nx.number_connected_components(connected),
        'modularity': nx.community.modularity(connected, groups, weight='weight'),
        'seed_ari_quantiles': same_resolution.quantile([.1,.5,.9]).tolist(),
        'full_counting_ari': adjusted_rand_score(reference, labels(full_groups, nodes)),
        'shared_author_list_flagged_papers': int(coverage.shared_author_affiliation_list.sum()),
        'networkx_version': nx.__version__, 'resolution': 1, 'seed': 534}
    (output / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary, indent=2))
    print(university_table.head(6).to_string(index=False))


if __name__ == '__main__':
    main()
