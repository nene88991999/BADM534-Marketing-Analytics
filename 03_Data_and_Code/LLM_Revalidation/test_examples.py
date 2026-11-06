import unittest
from summarize_snapshot import survival
from evaluate_upgrade import assess, zero_failure_upper
from evaluate_judges import compare


class Counterexamples(unittest.TestCase):
    def test_judge_reversal_changes_the_conclusion(self):
        result = compare({'old_judge': {'old_generator': 8, 'new_generator': 6},
                          'new_judge': {'old_generator': 4, 'new_generator': 7}})
        self.assertEqual(result['diagonal_change'], -1)
        self.assertEqual(result['generator_change_old_judge'], -2)
        self.assertEqual(result['generator_change_new_judge'], 3)

    def test_censoring_is_not_an_event(self):
        # At month 6: (5/6)*(3/4); the month-4 withdrawal changes the risk set.
        times, events = [2, 4, 6, 6, 8, 10], [1, 0, 1, 0, 1, 0]
        self.assertAlmostEqual(survival(times, events, 6), 5/8)
        self.assertAlmostEqual(survival(times, events, 8), 5/16)
        self.assertEqual(survival([1, 2], [0, 0], 2), 1)

    def test_same_average_can_conceal_a_regression(self):
        rows = [dict(case_id=1, old_pass=1, new_pass=0, failure_cost=10),
                dict(case_id=2, old_pass=0, new_pass=1, failure_cost=1)]
        result = assess(rows)
        self.assertEqual(result['net_gain_pp'], 0)
        self.assertEqual((result['old_loss'], result['new_loss']), (1, 10))
        self.assertEqual((result['improved'], result['regressed']), (1, 1))

    def test_zero_failures_has_a_positive_bound(self):
        self.assertAlmostEqual(zero_failure_upper(1), .95)
        self.assertAlmostEqual((1-zero_failure_upper(100))**100, .05)
        with self.assertRaises(ValueError):
            zero_failure_upper(0)


if __name__ == '__main__':
    unittest.main()
