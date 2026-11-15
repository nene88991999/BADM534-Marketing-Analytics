"""Small independent checks of the comparison's measurement rules."""
import unittest
import numpy as np
from centroid_checks import examples
from compare_clustering import make_data, nearest


class ClusteringChecks(unittest.TestCase):
    def test_count_weighted_ema(self):
        row = examples()
        self.assertEqual(row["ema_centroid"], "17/6")
        self.assertEqual(row["mean_of_centroids"], "9/2")

    def test_stale_assignment(self):
        row = examples()
        self.assertEqual(row["final_labels"], [0, 0, 1, 1])
        self.assertEqual(row["changed"], 1)
        self.assertEqual(row["final_assignment_mse"], "41/8")
        self.assertEqual(row["saved_assignment_mse"], "93/16")

    def test_independent_distances(self):
        labels, d2 = nearest([[0.], [4.], [10.]], [[0.], [10.]], chunk=2)
        np.testing.assert_array_equal(labels, [0, 0, 1])
        np.testing.assert_array_equal(d2, [0, 16, 0])

    def test_label_permutation_preserves_loss(self):
        first = nearest([[1.], [8.]], [[0.], [10.]])
        second = nearest([[1.], [8.]], [[10.], [0.]])
        np.testing.assert_array_equal(first[1], second[1])
        np.testing.assert_array_equal(first[0], 1 - second[0])

    def test_training_scale_and_repeatability(self):
        train, test = make_data(1000, 4)
        again, test_again = make_data(1000, 4)
        np.testing.assert_array_equal(train, again)
        np.testing.assert_array_equal(test, test_again)
        np.testing.assert_allclose(train.mean(axis=0), 0, atol=1e-6)
        np.testing.assert_allclose(train.std(axis=0), 1, atol=1e-6)
        self.assertEqual(test.shape, (200, 4))
        self.assertFalse(np.allclose(test.mean(axis=0), 0, atol=1e-6))


if __name__ == "__main__":
    unittest.main()
