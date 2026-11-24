"""Exact aggregation and travel calculations for four synthetic retail zones.

Run with Python 3.10+; standard library only. Paths are relative to this file.
Binary membership and combinatorial affinities are chosen explicitly.
"""
from fractions import Fraction as F
from pathlib import Path
import csv
import json
import math

HERE = Path(__file__).resolve().parent


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, col))
             for col in zip(*b)] for row in a]


def transpose(a):
    return list(map(list, zip(*a)))


def distances(n, edges):
    d = [[0 if i == j else math.inf for j in range(n)] for i in range(n)]
    for i, j, minutes in edges:
        assert minutes > 0 and i != j
        d[i][j] = d[j][i] = min(d[i][j], minutes)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


def calculate(case):
    names, group = case["zones"], case["group"]
    people = case["population"]
    x = [[F(v)] for v in case["weekly_zone_revenue_dollars"]]
    n, g = len(names), max(group) + 1
    assert len(group) == len(x) == len(people) == n
    assert set(group) == set(range(g)) and all(p > 0 for p in people)
    sizes = [group.count(c) for c in range(g)]
    q = [[int(c == group[i]) for c in range(g)] for i in range(n)]
    p = [[F(q[i][c], sizes[c]) for i in range(n)] for c in range(g)]
    means = multiply(p, x)
    reconstructed = multiply(q, means)
    a = [[F(0) for _ in range(n)] for _ in range(n)]
    for i, j, minutes in case["edges_minutes"]:
        a[i][j] = a[j][i] = F(1, minutes)
    coarse = multiply(multiply(transpose(q), a), q)
    for c in range(g):
        coarse[c][c] = F(0)
    coarse_edges = [(c, d, 1 / coarse[c][d]) for c in range(g)
                    for d in range(c + 1, g) if coarse[c][d] > 0]
    fine_d = distances(n, case["edges_minutes"])
    naive_d = distances(g, coarse_edges)
    store, threshold = case["store_node"], case["access_threshold_minutes"]
    rows = []
    for i, name in enumerate(names):
        fine, naive = fine_d[i][store], naive_d[group[i]][group[store]]
        rows.append(dict(zone=name, people=people[i], group=group[i],
                         revenue_dollars=float(x[i][0]),
                         reconstructed_revenue_dollars=float(reconstructed[i][0]),
                         original_minutes=float(fine), naive_coarse_minutes=float(naive),
                         original_access=int(fine <= threshold),
                         naive_coarse_access=int(naive <= threshold)))
    energy = sum(F(1, m) * (x[i][0] - x[j][0]) ** 2
                 for i, j, m in case["edges_minutes"])
    coarse_energy = sum(coarse[c][d] * (means[c][0] - means[d][0]) ** 2
                        for c in range(g) for d in range(c + 1, g))
    result = dict(
        synthetic=True, original_zones=n, groups=g, reduction=1 - g / n,
        group_sizes=sizes, group_mean_revenues=[float(v[0]) for v in means],
        original_mean_revenue=float(sum(v[0] for v in x) / n),
        equal_group_mean_revenue=float(sum(v[0] for v in means) / g),
        size_weighted_mean_revenue=float(sum(sizes[c] * means[c][0]
                                            for c in range(g)) / n),
        total_revenue=float(sum(v[0] for v in x)),
        sum_of_group_means=float(sum(v[0] for v in means)),
        reconstruction_squared_error=float(sum((x[i][0] - reconstructed[i][0]) ** 2
                                               for i in range(n))),
        original_energy=float(energy), coarse_energy=float(coarse_energy),
        energy_units="dollars squared per minute; weekly revenue feature",
        coarse_affinities=[[float(v) for v in row] for row in coarse],
        population=sum(people), access_threshold_minutes=threshold,
        original_access_share=sum(r["people"] * r["original_access"] for r in rows) / sum(people),
        naive_coarse_access_share=sum(r["people"] * r["naive_coarse_access"] for r in rows) / sum(people))
    return result, rows


def main():
    case = json.loads((HERE / "data/cases.json").read_text())["network"]
    result, rows = calculate(case)
    output = HERE / "results"
    output.mkdir(exist_ok=True)
    (output / "network.json").write_text(json.dumps(result, indent=2) + "\n")
    with (output / "zones.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
