"""Original arithmetic for the GraCo course review; no upstream imports or runs."""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json
import math


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def transpose(a):
    return list(map(list, zip(*a)))


def shortest_paths(n, edges):
    distance = [[0 if i == j else math.inf for j in range(n)] for i in range(n)]
    for i, j, minutes in edges:
        distance[i][j] = distance[j][i] = minutes
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance


def majority(labels):
    counts = Counter(labels)
    return min(counts, key=lambda x: (-counts[x], x))


def main():
    # Four invented retail zones, equal population, weekly revenues in dollars.
    # The first three zones form one supernode; the last forms the other.
    assignment = [0, 0, 0, 1]
    revenues = [[10], [10], [10], [40]]
    counts = [3, 1]
    q = [[int(c == assignment[i]) for c in range(2)] for i in range(4)]
    p = [[F(int(assignment[i] == c), counts[c]) for i in range(4)] for c in range(2)]
    coarse_revenues = multiply(p, revenues)
    assert multiply(p, q) == [[1, 0], [0, 1]]
    assert multiply(q, coarse_revenues) == revenues
    fine_mean = F(sum(x[0] for x in revenues), 4)
    coarse_equal_mean = sum(x[0] for x in coarse_revenues) / 2
    coarse_weighted_mean = sum(counts[c] * coarse_revenues[c][0] for c in range(2)) / 4
    assert fine_mean == coarse_weighted_mean == F(35, 2)
    assert coarse_equal_mean == 25
    fine_total = sum(x[0] for x in revenues)
    sum_of_means = sum(x[0] for x in coarse_revenues)
    assert fine_total == 70 and sum_of_means == 50
    aggregation = dict(zone_revenues=[r[0] for r in revenues], supernode_sizes=counts,
                       supernode_means=[float(x[0]) for x in coarse_revenues],
                       fine_mean=float(fine_mean), equal_supernode_mean=float(coarse_equal_mean),
                       size_weighted_mean=float(coarse_weighted_mean),
                       fine_total=fine_total, sum_of_supernode_means=float(sum_of_means))

    # Travel minutes and graph affinities have distinct units: affinity = 1/minutes.
    edges = [(0, 1, 4), (1, 2, 1), (2, 3, 4)]
    adjacency = [[F(0) for _ in range(4)] for _ in range(4)]
    for i, j, minutes in edges:
        adjacency[i][j] = adjacency[j][i] = F(1, minutes)
    coarse_adjacency = multiply(multiply(transpose(q), adjacency), q)
    for i in range(2):
        coarse_adjacency[i][i] = F(0)
    assert coarse_adjacency[0][1] == F(1, 4)
    fine_energy = sum(F(1, m) * (revenues[i][0] - revenues[j][0]) ** 2 for i, j, m in edges)
    coarse_energy = coarse_adjacency[0][1] * (coarse_revenues[0][0] - coarse_revenues[1][0]) ** 2
    assert fine_energy == coarse_energy == 225

    fine_distance = shortest_paths(4, edges)
    # This reciprocal interpretation discards travel inside a supernode.
    naive_coarse_minutes = 1 / coarse_adjacency[0][1]
    fine_access = [fine_distance[i][3] <= 5 for i in range(4)]
    coarse_access = [assignment[i] == 1 or naive_coarse_minutes <= 5 for i in range(4)]
    assert fine_distance[0][3] == 9 and naive_coarse_minutes == 4
    assert sum(fine_access) == 3 and sum(coarse_access) == 4
    preservation = dict(fine_energy=float(fine_energy), coarse_energy=float(coarse_energy),
                        fine_origin_to_store_minutes=9, naive_coarse_minutes=4,
                        threshold_minutes=5, fine_access_share=0.75, naive_coarse_access_share=1.0)

    # Global majority uses all labels. A split score uses that same majority.
    labels = [0, 0, 1]
    global_label = majority(labels)
    train = [2]
    test = [0, 1]
    trained_label = majority([labels[i] for i in train])
    oracle_test_score = sum(labels[i] == global_label for i in test) / len(test)
    trained_test_score = sum(labels[i] == trained_label for i in test) / len(test)
    assert oracle_test_score == 1 and trained_test_score == 0
    # If the test subset contains only node 2, its own best constant is label 1.
    assert int(labels[2] == global_label) == 0
    assert int(labels[2] == majority([labels[2]])) == 1
    # Two invented groups, each with three class-0 and one class-1 customer.
    minority_labels = [0, 0, 0, 1, 0, 0, 0, 1]
    prediction = [majority(minority_labels[:4])] * 4 + [majority(minority_labels[4:])] * 4
    accuracy = sum(a == b for a, b in zip(prediction, minority_labels)) / 8
    minority_recall = sum(a == 1 and b == 1 for a, b in zip(prediction, minority_labels)) / 2
    assert accuracy == 0.75 and minority_recall == 0
    label_checks = dict(global_label=global_label, training_only_label=trained_label,
                        global_majority_test_score=oracle_test_score,
                        training_only_test_score=trained_test_score,
                        other_subset_global_majority_score=0, other_subset_own_ceiling=1,
                        mixed_groups_accuracy=accuracy, minority_recall=minority_recall)

    # A three-node path has two undirected edges, each counted once here.
    # Changing only node 2's held-out label changes the all-edge heterophily.
    path_edges = [(0, 1), (1, 2)]
    def alpha(y):
        return sum(y[i] != y[j] for i, j in path_edges) / len(path_edges)
    assert alpha([0, 0, 0]) == 0 and alpha([0, 0, 1]) == 0.5
    label_parameter = dict(before_test_label_change=0.0, after_test_label_change=0.5)

    # Recalculate the already documented M5 Section 5.21 synthetic case.
    retained_share = F(550, 800 - 150)
    original_share = F(550, 800)
    assert original_share == F(11, 16) and retained_share == F(11, 13)
    denominator = dict(original_people=800, removed_people=150, people_with_known_access=550,
                       original_share=float(original_share), retained_component_share=float(retained_share),
                       percentage_point_change=float(100 * (retained_share - original_share)))

    # Selected published Cora rows, Table 4, PDF page 25; these are not new fits.
    published = {'Local Variation': {'r': 0.70, 'rsa': 0.67, 'cme_thousands': 32.9},
                 'Leiden': {'r': 0.70, 'rsa': 1.58, 'cme_thousands': 29.2}}
    assert min(published, key=lambda m: published[m]['rsa']) == 'Local Variation'
    assert min(published, key=lambda m: published[m]['cme_thousands']) == 'Leiden'
    result = dict(scope='Original exact calculations and selected published-table comparisons; no GraCo execution.',
                  checks_passed=7, checks=['size-weighted aggregation', 'block-constant energy',
                  'travel and threshold access', 'global-label and subgroup diagnostics',
                  'label-dependent preprocessing parameter', 'component denominator', 'metric ranking'],
                  aggregation=aggregation, preservation=preservation, labels=label_checks,
                  label_parameter=label_parameter, denominator=denominator, published_cora_rows=published)
    (Path(__file__).resolve().parent / 'source_checks.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
