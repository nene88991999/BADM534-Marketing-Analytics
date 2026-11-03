"""Counterexample checks for missingness, weighting, matching, and event windows."""
import unittest
import pandas as pd
from assessment import HERE, load_checked, firm_coverage
from disclosure import role_rates
from event_windows import compare_windows
from construct_checks import match_terms


class MeasurementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.calls, cls.mentions, cls.firms, cls.dictionary = load_checked()

    def test_missing_text_is_unknown(self):
        row = self.calls.set_index('call_id').loc['DLTR_FY2026Q2']
        self.assertFalse(row.text_observed)
        self.assertTrue(pd.isna(row.has_core))

    def test_empty_roster_member_is_retained(self):
        out = firm_coverage(self.calls, self.firms).set_index('ticker')
        self.assertEqual(len(out), 123)
        self.assertEqual(out.loc['WINA', 'calls_observed'], 0)
        self.assertTrue(pd.isna(out.loc['WINA', 'core_call_rate']))
        self.assertTrue(out.loc[out.calls_observed.gt(0), 'core_call_rate'].eq(0).any())

    def test_positive_only_join_changes_estimand(self):
        self.assertAlmostEqual(self.calls.has_core.mean(), 112 / 2325)
        self.assertAlmostEqual(self.calls.loc[self.calls.has_any, 'has_core'].mean(), 112 / 445)

    def test_role_numerator_and_exposure_share_sample(self):
        calls = pd.DataFrame({'call_id': ['a', 'b'], 'text_observed': [True, True],
                              'qa_detected': [True, False],
                              'words_management': [100, 900], 'words_analyst': [100, 0]})
        mentions = pd.DataFrame({'call_id': ['a', 'b'], 'tier': ['core', 'core'],
                                'role': ['management', 'management']})
        row = role_rates(calls, mentions, True).set_index('role').loc['management']
        self.assertEqual(row.core_matches, 1)
        self.assertEqual(row.words, 100)
        self.assertEqual(row.per_10000_words, 100)

    def test_event_day_and_boundaries(self):
        d = pd.DataFrame({'call_date': pd.to_datetime(['2024-02-25', '2024-02-26',
                              '2024-02-27', '2024-02-28', '2024-02-29', '2024-03-01']),
                          'ticker': ['A']*6, 'group': ['retail']*6,
                          'text_observed': [True]*6, 'has_core': [1.0]*6, 'n_core': [2]*6})
        out = compare_windows(d, days=2)
        self.assertTrue(out.calls.eq(2).all())
        self.assertTrue(out.core_matches.eq(4).all())

    def test_equal_firm_and_call_weights_differ(self):
        d = pd.DataFrame({'call_date': pd.to_datetime(['2024-03-01']*3),
                          'ticker': ['A', 'A', 'B'], 'group': ['retail']*3,
                          'text_observed': [True]*3, 'has_core': [1.0, 1.0, 0.0], 'n_core': [1,1,0]})
        out = compare_windows(d).iloc[0]
        self.assertAlmostEqual(out.share_percent, 200/3)
        self.assertEqual(out.firm_equal_share_percent, 50)

    def test_denial_is_still_a_dictionary_hit(self):
        self.assertIn('dynamic_pricing', match_terms('We do not use dynamic pricing.', self.dictionary))
        self.assertEqual(match_terms('Our fares adjust every hour with demand.', self.dictionary), [])

    def test_original_dictionary_case_sensitivity(self):
        self.assertIn('esl_acronym', match_terms('ESL tags', self.dictionary))
        self.assertNotIn('esl_acronym', match_terms('esl tags', self.dictionary))

    def test_metadata_export_excludes_transcript_text(self):
        for name in ['calls', 'mentions', 'firms']:
            columns = pd.read_csv(HERE / 'data' / (name + '.csv'), nrows=0).columns
            self.assertTrue({'sentence', 'context', 'speaker', 'matched_text', 'title'}.isdisjoint(columns))


if __name__ == '__main__':
    unittest.main()
