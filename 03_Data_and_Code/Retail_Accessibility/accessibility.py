"""Synthetic service restoration, accessibility bounds, and graph comparisons."""
from pathlib import Path
import csv
import json
import math
import networkx as nx

HERE = Path(__file__).resolve().parent
POSITIONS = {"W0": (0, 0), "W1": (0, 2), "W2": (0, 4),
             "E0": (1, 0), "E1": (1, 2), "E2": (1, 4), "X": (4, 0)}
PEOPLE = {"W0": 100, "W1": 300, "W2": 100, "E0": 50,
          "E1": 50, "E2": 50, "X": 150}
STORES = {"A": "W0", "B": "E0", "C": "W2", "D": "E2", "U": "X"}
STATUS = {"A": 0, "B": 1, "C": 1, "D": 0, "U": None}
PROFIT = {"A": 20, "D": 40}  # Imposed incremental weekly dollars, equal costs.


def write_csv(path, rows):
    with Path(path).open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]),
                                lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def graph():
    g = nx.Graph()
    g.add_nodes_from(POSITIONS)
    g.add_weighted_edges_from([("W0", "W1", 4), ("W1", "W2", 4),
                               ("E0", "E1", 4), ("E1", "E2", 4),
                               ("W2", "E2", 2)], weight="minutes")
    return g


def distances(g, metric="network"):
    if metric not in {"network", "straight"}:
        raise ValueError("Use network or straight distance")
    paths = dict(nx.all_pairs_dijkstra_path_length(g, weight="minutes"))
    return {(a, b): (paths[a].get(b, math.inf) if metric == "network"
                     else 2 * math.dist(POSITIONS[a], POSITIONS[b]))
            for a in POSITIONS for b in POSITIONS}


def access_rows(distance, status, threshold=5):
    if any(s not in (0, 1, None) for s in status.values()):
        raise ValueError("Availability must be 0, 1, or None")
    rows = []
    for origin, people in PEOPLE.items():
        certain = [distance[origin, STORES[s]] for s, v in status.items() if v == 1]
        possible = [distance[origin, STORES[s]] for s, v in status.items() if v != 0]
        best = min(certain, default=math.inf)
        rows.append(dict(origin=origin, people=people,
                         known_minutes=best if math.isfinite(best) else None,
                         lower=int(best <= threshold),
                         upper=int(min(possible, default=math.inf) <= threshold)))
    return rows


def summarize(rows):
    denominator = sum(r["people"] for r in rows)
    return {"people": denominator,
            "lower_people": sum(r["people"] * r["lower"] for r in rows),
            "upper_people": sum(r["people"] * r["upper"] for r in rows)}


def nearest_edges(distance, nodes, k):
    if not 0 < k < len(nodes):
        raise ValueError("k must be between 1 and n-1")
    return {(a, b) for a in nodes for b in
            sorted((b for b in nodes if b != a), key=lambda b: (distance[a, b], b))[:k]
            if math.isfinite(distance[a, b])}


def main(output=HERE / "results"):
    output = Path(output); output.mkdir(parents=True, exist_ok=True)
    g = graph(); net = distances(g); straight = distances(g, "straight")
    origins, policies = [], []
    for policy in ["Baseline", "Restore A", "Restore D"]:
        status = STATUS.copy()
        if policy != "Baseline":
            status[policy[-1]] = 1
        rows = access_rows(net, status)
        origins.extend(dict(policy=policy, **r) for r in rows)
        result = summarize(rows)
        result["lower_share"] = result["lower_people"] / result["people"]
        result["upper_share"] = result["upper_people"] / result["people"]
        result["profit_gain"] = PROFIT.get(policy[-1], 0)
        result["known_unavailable_share"] = sum(v == 0 for v in status.values()) / sum(v is not None for v in status.values())
        policies.append(dict(policy=policy, **result))
    banks = sorted(n for n in POSITIONS if n != "X")
    edge_rows, comparisons = [], []
    for k in [1, 2]:
        edges = {m: nearest_edges(d, banks, k)
                 for m, d in [("straight", straight), ("network", net)]}
        for metric, pairs in edges.items():
            edge_rows.extend(dict(k=k, metric=metric, origin=a, target=b,
                                  network_minutes=net[a, b]) for a, b in sorted(pairs))
        comparisons.append(dict(k=k, directed_edges=len(edges["network"]),
                                common_edges=len(edges["network"] & edges["straight"]),
                                straight_neighbors_network_minutes=sum(net[e] for e in edges["straight"]) / len(edges["straight"]),
                                network_neighbors_network_minutes=sum(net[e] for e in edges["network"]) / len(edges["network"])))
    write_csv(output / "synthetic_origins.csv", origins)
    write_csv(output / "policies.csv", policies)
    write_csv(output / "neighbors.csv", edge_rows)
    write_csv(output / "neighbor_comparison.csv", comparisons)
    result = {"synthetic": True, "threshold_minutes": 5, "known_store_unavailability": 0.5,
              "unknown_store_records": 1, "network_baseline": summarize(access_rows(net, STATUS)),
              "straight_baseline": summarize(access_rows(straight, STATUS)),
              "policies": policies, "neighbor_comparison": comparisons}
    (output / "synthetic_summary.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "results")
    main(parser.parse_args().output)
