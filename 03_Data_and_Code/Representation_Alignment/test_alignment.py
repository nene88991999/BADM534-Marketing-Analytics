"""Independent small cases and checks against the executed mHealth outputs."""
import csv
import json
import unittest
from collections import Counter
from pathlib import Path
import numpy as np
from alignment import apply_map, fit_map, neighbors, neighbor_overlap, synthetic_case
from evaluate_mhealth import encode, metrics, predict, reduce_fit, train_classifier
from prepare_descriptions import normalize, partition, summarize

HERE = Path(__file__).resolve().parent


class AlignmentTests(unittest.TestCase):
    def test_known_affine_rotation_on_new_points(self):
        x = np.array([[-2, -1], [-2, 1], [2, -1], [2, 1]], float)
        q = np.array([[0., 1.], [-1., 0.]])
        y = 3 * x @ q + [7, -4]
        fitted = fit_map(x, y)
        fresh = np.array([[1, 8], [-6, 3]], float)
        np.testing.assert_allclose(apply_map(fresh, fitted), 3*fresh@q+[7, -4], atol=1e-12)
        np.testing.assert_allclose(fitted[2].T @ fitted[2], np.eye(2), atol=1e-12)

    def test_degenerate_and_unpaired_inputs(self):
        with self.assertRaises(ValueError): fit_map(np.zeros((3, 2)), np.ones((3, 2)))
        with self.assertRaises(ValueError): fit_map(np.ones((3, 2)), np.ones((2, 2)))
        with self.assertRaises(ValueError): fit_map([[1, 2], [3, float('nan')]], [[1, 2], [3, 4]])

    def test_exact_rotation_and_distance_ranking(self):
        r = synthetic_case()
        scores = {x['name']: x for x in r['results']}
        self.assertEqual(scores['rotated_unmapped']['correct'], 4)
        self.assertEqual(scores['compressed_style']['correct'], 8)
        self.assertEqual(scores['rotated_unmapped']['neighbor_overlap_k2'], 1)
        self.assertEqual(scores['compressed_style']['neighbor_overlap_k2'], 0.5)
        x, z = np.array(r['test']), np.array(scores['rotated_unmapped']['values'])
        for i in range(8):
            for j in range(8):
                self.assertAlmostEqual(sum((x[i]-x[j])**2), sum((z[i]-z[j])**2))

    def test_ties_and_self_exclusion(self):
        x = np.array([[0.], [0.], [1.], [-1.]])
        self.assertEqual(neighbors(x, 2)[0].tolist(), [1, 2])
        for i, indices in enumerate(neighbors(x, 3)): self.assertNotIn(i, indices)
        self.assertAlmostEqual(neighbor_overlap(x, 4*x+2, 2), 1)

    def test_normalization_and_modal_labels(self):
        self.assertEqual(normalize('  OAT\n Milk '), 'oat milk')
        r = summarize({'oat milk': Counter({'B': 2, 'A': 2})})[0]
        self.assertEqual((r['category'], r['category_count'], r['source_entries']), ('A', 2, 4))
        self.assertEqual(r['split'], partition('oat milk')[0])

    def test_training_vocabulary_stays_fixed(self):
        x, state = encode(['rice rice', 'milk'], 'word')
        expected = dict(state[0])
        z, _ = encode(['unseenword'], 'word', state)
        self.assertEqual(state[0], expected)
        self.assertEqual(float(np.linalg.norm(z)), 0)
        basis = reduce_fit(x, 2)
        np.testing.assert_allclose(basis.T @ basis, np.eye(2), atol=1e-12)

    def test_classifier_and_unseen_category_denominators(self):
        x = np.array([[-2.], [-1.], [1.], [2.]])
        classes, y = ['A', 'B'], ['A', 'A', 'B', 'B']
        pred = predict(x, train_classifier(x, y, classes), classes)
        self.assertEqual(pred.tolist(), y)
        m = metrics(['A', 'A', 'B', 'C'], ['A', 'B', 'B', 'A'], classes)
        self.assertEqual(m['correct'], 2)
        self.assertEqual(sum(r['support'] for r in m['by_category']), 4)
        self.assertEqual(next(r for r in m['by_category'] if r['category']=='C')['recall'], 0)

    def test_sample_splits_are_disjoint_and_label_independent(self):
        with (HERE/'data/descriptions.csv').open(newline='') as stream: rows=list(csv.DictReader(stream))
        self.assertEqual(len({r['description'] for r in rows}), len(rows))
        self.assertEqual(Counter(r['split'] for r in rows), {'train':6000, 'validation':1500, 'test':1500})
        for r in rows: self.assertEqual(r['split'], partition(r['description'])[0])

    def test_saved_predictions_reproduce_counts_by_category(self):
        r=json.loads((HERE/'results/mhealth.json').read_text())
        with (HERE/'results/test_predictions.csv').open(newline='') as stream: rows=list(csv.DictReader(stream))
        for name, score in r['primary_test'].items():
            correct=sum(row['reference_category']==row[name] for row in rows)
            self.assertEqual((score['cases'],score['correct']), (len(rows),correct))
            for category in score['by_category']:
                subset=[x for x in rows if x['reference_category']==category['category']]
                self.assertEqual(category['support'],len(subset))
                self.assertEqual(category['correct'],sum(x[name]==x['reference_category'] for x in subset))
        val=r['validation']
        chosen=min(val,key=lambda x:(-x['accuracy'],x['dimension']))['dimension']
        self.assertEqual(chosen,r['selected_dimension'])
        self.assertTrue(all('test' not in v for k,v in r['all_configurations'].items() if int(k)!=chosen))
        m=r['primary_test']
        self.assertAlmostEqual(m['character_aligned']['neighbor_overlap_k10'],m['character_unmapped']['neighbor_overlap_k10'])


if __name__ == '__main__': unittest.main()
