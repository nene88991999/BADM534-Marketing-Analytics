"""Independent hand calculations, invariances, denominators, and log boundaries."""
import csv
import json
import math
from pathlib import Path
import tempfile
import unittest

import mixture_regression as mixture
import service_contexts as service
import source_checkpoint_comparison as published


class MixtureChecks(unittest.TestCase):
    def test_original_feature_normal_equations(self):
        # Two A rows (2,1), three B rows (2,0), lambda=8, y_A=1, y_B=0.
        # X'X+8I = [[28,4],[4,10]], X'y=[4,2], determinant=264.
        task, tag = mixture.fit(2, 3, 1, a=2, c=8)
        self.assertAlmostEqual(task, 2 * (40 - 8) / 264)
        self.assertAlmostEqual(tag, (56 - 16) / 264)

    def test_unrelated_examples_and_zero_source(self):
        self.assertEqual(mixture.fit(5, 0, 0), mixture.fit(5, 1000, 0))
        self.assertEqual(mixture.fit(0, 30, 1), (0, 0))

    def test_matched_contrast_and_penalty_scaling(self):
        task0, tag0 = mixture.fit(5000, 0, 1)
        task1, tag1 = mixture.fit(5000, 100000, 1)
        self.assertLess(task1, task0)
        self.assertGreater(tag1, tag0)
        original = mixture.fit(5, 12, .1, 2, 8)
        scaled = mixture.fit(50, 120, .1, 20, 80)
        for a, b in zip(original, scaled):
            self.assertAlmostEqual(a, b)

    def test_fixed_total_exact_maximum(self):
        n, q, a, c = 30000, .1, 50, 1500
        optimum = (q + a / n) / (q + math.sqrt(q))
        target = mixture.fit(optimum*n, (1-optimum)*n, q, a, c)[1]
        for shift in [-.01, .01]:
            x = optimum + shift
            self.assertLess(mixture.fit(x*n, (1-x)*n, q, a, c)[1], target)

    def test_invalid_inputs(self):
        for args in [(-1, 2, 1), (2, -1, 1), (2, 2, 1.1), (2, 2, 1, 0, 1)]:
            with self.assertRaises(ValueError):
                mixture.fit(*args)


class ServiceChecks(unittest.TestCase):
    def test_population_pairing_and_aggregate_identity(self):
        records = service.make_records()
        self.assertEqual(len(records), 2000)
        self.assertEqual(len({r['request_id'] for r in records}), 1000)
        self.assertEqual(service.paired_changes(records),
                         {'paired_requests': 1000, 'recoveries': 27, 'regressions': 27})
        totals = [r for r in service.summarize(records) if r['context'] == 'all']
        self.assertEqual([r['correct'] for r in totals], [950, 950])

    def test_context_rates_and_missing_denominator(self):
        rows = service.summarize(service.make_records())
        row = next(r for r in rows if r['version'] == 'combined'
                   and r['context'] == 'cancellation')
        self.assertEqual((row['correct'], row['attempted'], row['missing']), (8, 20, 5))
        self.assertAlmostEqual(row['rate_per_attempt'], .4)
        self.assertAlmostEqual(row['rate_per_response'], 8/15)
        combined = next(r for r in rows if r['version'] == 'combined' and r['context'] == 'all')
        self.assertAlmostEqual(combined['rate_per_attempt'], .95)
        self.assertAlmostEqual(combined['rate_per_response'], 950/985)

    def test_empty_and_incomplete_pairs(self):
        self.assertTrue(all(r['rate_per_attempt'] is None for r in service.summarize([])))
        with self.assertRaises(ValueError):
            service.paired_changes([{'request_id': 'a', 'version': 'original',
                                     'correct_resolution': 1}])
        with self.assertRaises(ValueError):
            service.paired_changes(service.make_records()[:1] * 2)


class PublishedChecks(unittest.TestCase):
    def test_resumed_epoch_and_missing_epoch(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'curve.jsonl'
            rows = [dict(epoch=i, trigger=i/100) for i in range(1, 11)]
            rows.append(dict(epoch=2, trigger=.9))
            p.write_text('\n'.join(json.dumps(row) for row in rows))
            epochs, count = published.last_per_epoch(p)
            self.assertEqual((epochs[2]['trigger'], count, len(epochs)), (.9, 11, 10))
            p.write_text(json.dumps(dict(epoch=10, trigger=.1)))
            with self.assertRaises(ValueError):
                published.last_per_epoch(p)

    def test_saved_source_rates(self):
        with (published.ROOT / 'results/published_checkpoints.csv').open() as stream:
            rows = [r for r in csv.DictReader(stream) if r['condition'] == '9000_A_21000_B']
        self.assertEqual([float(r['final_rate']) for r in rows], [.54, .54, .68])
        self.assertEqual([float(r['peak_rate']) for r in rows], [.66, .58, .82])


if __name__ == '__main__':
    unittest.main()
