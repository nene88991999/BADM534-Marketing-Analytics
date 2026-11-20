"""Independent arithmetic, information-boundary, and population checks."""
import csv
import json
import unittest
from pathlib import Path

import retail_monitoring as monitoring
import timing_and_missingness as timing

ROOT = Path(__file__).resolve().parent


class ExampleChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.events = monitoring.make_data()

    def test_population_and_intervals(self):
        keys = {(r['store'], r['day'], r['minute']) for r in self.rows}
        self.assertEqual(len(keys), 4320)
        self.assertEqual([sum(r['split'] == s for r in self.rows)
                          for s in ('train', 'validation', 'test')], [2160, 1080, 1080])
        for event in self.events:
            self.assertEqual(event['end'] - event['start'], 20)
        self.assertEqual(sum(r['latency_ms'] is None for r in self.rows), 3)

    def test_information_boundary(self):
        reference = monitoring.fit_reference([r for r in self.rows if r['split'] == 'train'])
        early = dict(next(r for r in self.rows if r['latency_ms'] is None))
        first = monitoring.score_rows([early], reference)[0]
        future = dict(early, minute=100, latency_ms=999999)
        second = monitoring.score_rows([early, future], reference)[0]
        self.assertEqual(first, second)
        self.assertEqual(first['missing_features'], 1)
        self.assertEqual(first['deviations']['latency_ms'], 0)

    def test_nominal_validation_tail(self):
        fit = monitoring.fit_reference([r for r in self.rows if r['split'] == 'train'])
        validation = monitoring.score_rows([r for r in self.rows if r['split'] == 'validation'], fit)
        thresholds = monitoring.calibrate(validation)
        for method, threshold in thresholds.items():
            self.assertLessEqual(sum(r[method] > threshold for r in validation), 10)

    def test_saved_detection_counts(self):
        scores = list(csv.DictReader((ROOT / 'results/test_scores.csv').read_text().splitlines()))
        summaries = list(csv.DictReader((ROOT / 'results/detection_summary.csv').read_text().splitlines()))
        positives = {(e['store'], e['day'], t) for e in self.events
                     for t in range(e['start'], e['end'])}
        event_runs = {(e['store'], e['day']) for e in self.events}
        for summary in summaries:
            alerts = {(r['store'], int(r['day']), int(r['minute'])) for r in scores
                      if float(r[summary['method']]) > float(summary['threshold'])}
            self.assertEqual(int(summary['tp']), len(alerts & positives))
            self.assertEqual(int(summary['fp']), len(alerts - positives))
            self.assertEqual(int(summary['fn']), len(positives - alerts))
            self.assertEqual(int(summary['tn']), 1080 - len(alerts | positives))
            nominal = [r for r in scores if (r['store'], int(r['day'])) not in event_runs]
            self.assertEqual(len(nominal), 720)
            self.assertEqual(int(summary['nominal_alert_minutes']),
                             sum(float(r[summary['method']]) > float(summary['threshold']) for r in nominal))

    def test_timing_by_set_arithmetic(self):
        truth = set(range(40, 60))
        for span in [(40, 60), (45, 65), (0, 120), (60, 80)]:
            predicted = set(range(*span))
            result = timing.interval_metrics(span, (40, 60))
            self.assertEqual(result['any_overlap'], int(bool(predicted & truth)))
            self.assertAlmostEqual(result['interval_iou'], len(predicted & truth) / len(predicted | truth))
        with self.assertRaises(ValueError):
            timing.interval_metrics((40, 40), (40, 60))

    def test_missingness_uses_past_information(self):
        for future in (90, 900):
            values = [None, None, future, 92]
            self.assertEqual(timing.causal_fill(values, 100)[:2], [100, 100])
            self.assertEqual(timing.forward_then_backward(values)[:2], [future, future])
        self.assertEqual(timing.causal_fill([10, None, 15], 100), [10, 10, 15])

    def test_packets_preserve_normal_runs_without_answers(self):
        packets = json.loads((ROOT / 'results/evidence_packets.json').read_text())
        self.assertEqual(len(packets), 9)
        self.assertEqual(sum(len(p['measurements']) for p in packets), 1080)
        for packet in packets:
            self.assertNotIn('cause', packet)
            for record in packet['measurements']:
                self.assertEqual(set(record), {'timestamp', 'minute', *monitoring.FEATURES})

    def test_beneficial_campaign_is_also_unusual(self):
        results = list(csv.DictReader((ROOT / 'results/incident_metrics.csv').read_text().splitlines()))
        campaign = [r for r in results if r['cause'] == 'campaign']
        self.assertEqual(len(campaign), 2)
        self.assertTrue(all(r['detected'] == 'True' for r in campaign))
        self.assertTrue(all(float(r['delay_minutes']) == 0 for r in campaign))


if __name__ == '__main__':
    unittest.main()
