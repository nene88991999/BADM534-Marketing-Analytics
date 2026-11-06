import unittest
import numpy as np
import pandas as pd
from cluster import FEATURES, select_sample, partition
from affiliation_clusters import make_graph, communities


class AnalysisTests(unittest.TestCase):
    def test_affiliation_projection_preserves_paper_mass(self):
        pairs = pd.DataFrame({'paper_id': ['p1', 'p1', 'p1', 'p2', 'p3', 'p3'],
                              'institution_id': ['A', 'B', 'C', 'D', 'A', 'B']})
        graph = make_graph(pairs)
        self.assertAlmostEqual(graph.size(weight='weight'), 2)
        self.assertAlmostEqual(graph['A']['B']['weight'], 4/3)
        self.assertEqual(graph.degree('D'), 0)
        connected, groups = communities(graph)
        self.assertNotIn('D', connected)
        self.assertEqual(set().union(*groups), {'A', 'B', 'C'})

    def test_jaccard_ignores_shared_absences(self):
        x = np.array([[1, 1, 0], [1, 0, 0], [0, 0, 1]])
        labels, distance = partition(x, 2)
        self.assertAlmostEqual(distance[0, 1], .5)
        self.assertAlmostEqual(distance[0, 2], 1)
        self.assertEqual(labels[0], labels[1])
        extended = np.column_stack([x, np.zeros((3, 5))])
        np.testing.assert_allclose(distance, partition(extended, 2)[1])

    def test_access_and_unknowns_change_sample(self):
        rows = []
        for i, (status, access) in enumerate([
            ("potential_dual_use", "downloaded"), ("potential_dual_use", "unavailable"),
            ("not_reviewed", "unavailable"), ("protective", "downloaded")]):
            row = dict.fromkeys(FEATURES, 0)
            row.update(id=str(i), review_status=status, download_status=access, social_cues=1)
            rows.append(row)
        data = pd.DataFrame(rows)
        self.assertEqual(select_sample(data, "downloaded_risk").id.tolist(), ["0"])
        self.assertEqual(select_sample(data, "all_reviewed_risk").id.tolist(), ["0", "1"])
        self.assertEqual(select_sample(data, "downloaded_with_protective").id.tolist(), ["0", "3"])
        data.loc[0, "social_cues"] = np.nan
        with self.assertRaises(ValueError):
            select_sample(data, "downloaded_risk")


if __name__ == "__main__":
    unittest.main()
