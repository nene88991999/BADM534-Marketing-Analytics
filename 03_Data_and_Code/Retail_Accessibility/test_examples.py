"""Independent checks for units, reachability, missing status, and graph rules."""
import itertools
import math
import unittest
import networkx as nx
from accessibility import (graph, distances, access_rows, summarize, nearest_edges,
                           STATUS, STORES, POSITIONS)
from snapshot_access import haversine, build_network


class ExampleTests(unittest.TestCase):
    def test_shortest_paths_against_path_enumeration(self):
        g = graph(); d = distances(g)
        for a, b in itertools.permutations(g, 2):
            paths = list(nx.all_simple_paths(g, a, b))
            expected = min((sum(g[u][v]["minutes"] for u, v in zip(p, p[1:]))
                            for p in paths), default=math.inf)
            self.assertEqual(d[a, b], expected)
        self.assertEqual(d["W0", "E0"], 18)

    def test_bounds_against_all_missing_status_completions(self):
        d = distances(graph()); bounds = summarize(access_rows(d, STATUS))
        completed = [summarize(access_rows(d, dict(STATUS, U=s)))["lower_people"] for s in [0, 1]]
        self.assertEqual([bounds["lower_people"], bounds["upper_people"]], [min(completed), max(completed)])
        self.assertEqual(completed, [550, 700])

    def test_isolated_origin_remains_in_denominator(self):
        rows = access_rows(distances(graph()), STATUS)
        self.assertEqual(summarize(rows)["people"], 800)
        x = next(r for r in rows if r["origin"] == "X")
        self.assertEqual((x["lower"], x["upper"], x["known_minutes"]), (0, 1, None))

    def test_restoration_same_store_rate_different_access(self):
        d = distances(graph())
        results = [summarize(access_rows(d, dict(STATUS, **{s: 1}))) for s in ["A", "D"]]
        self.assertEqual([r["lower_people"] for r in results], [650, 550])
        for s in ["A", "D"]:
            status = dict(STATUS, **{s: 1})
            self.assertEqual(sum(x == 0 for x in status.values()), 1)

    def test_availability_monotonicity(self):
        d = distances(graph()); keys = list(STORES)
        for values in itertools.product([0, 1], repeat=len(keys)):
            status = dict(zip(keys, values)); before = summarize(access_rows(d, status))["lower_people"]
            for key in keys:
                after = summarize(access_rows(d, dict(status, **{key: 1})))["lower_people"]
                self.assertGreaterEqual(after, before)

    def test_neighbor_count_and_fixed_metric_comparison(self):
        nodes = sorted(set(POSITIONS) - {"X"}); d = distances(graph())
        e = nearest_edges(distances(graph(), "straight"), nodes, 1)
        n = nearest_edges(d, nodes, 1)
        self.assertEqual(len(e), 6); self.assertEqual(len(n), 6)
        self.assertEqual(len(e & n), 2)
        self.assertAlmostEqual(sum(d[p] for p in e)/6, 10)
        self.assertAlmostEqual(sum(d[p] for p in n)/6, 10/3)

    def test_geographical_distance_units(self):
        self.assertAlmostEqual(haversine((0, 0), (0, 1)), 111.1950802335, places=6)
        self.assertEqual(haversine((40, -88), (40, -88)), 0)

    def test_access_tags_and_boundary(self):
        nodes = [dict(type="node", id=i, lat=40.10, lon=-88.24+i*.001) for i in range(5)]
        nodes.append(dict(type="node", id=5, lat=41.0, lon=-88.24))
        ways = [dict(type="way", id=1, nodes=[0, 1], tags={"highway": "residential"}),
                dict(type="way", id=2, nodes=[1, 2], tags={"highway": "service", "access": "private"}),
                dict(type="way", id=3, nodes=[2, 3], tags={"highway": "footway", "access": "private", "foot": "yes"}),
                dict(type="way", id=4, nodes=[3, 4], tags={"highway": "residential", "foot": "no"}),
                dict(type="way", id=5, nodes=[0, 5], tags={"highway": "residential"})]
        g = build_network({"elements": nodes+ways})
        self.assertEqual({frozenset(e) for e in g.edges}, {frozenset([0, 1]), frozenset([2, 3])})


if __name__ == "__main__":
    unittest.main()
