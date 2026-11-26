"""Independent checks of source handling, denominators, and bill arithmetic."""
import unittest
from decimal import Decimal
from collect import VisibleText, extract, candidates
from analyze import load_inputs, coverage, comparison_matrix, bill_calculations


class EvidenceChecks(unittest.TestCase):
    def test_hidden_markup_is_excluded(self):
        parser = VisibleText()
        parser.feed('<head>irrelevant rate</head><p>Visible</p>'
                    '<script>hidden recovery</script><style>hidden bill</style>')
        self.assertEqual(''.join(parser.parts).strip(), 'Visible')

    def test_wrong_document_is_rejected(self):
        spec = dict(format='html', start_marker='Start', end_marker='Stop',
                    identity_markers=['Expected issuer'])
        with self.assertRaises(ValueError):
            extract(('<p>Start ' + 'Other issuer ' * 60 + ' Stop</p>').encode(), spec)

    def test_navigation_and_footer_are_excluded(self):
        spec = dict(format='html', start_marker='Opening', end_marker='Footer',
                    identity_markers=['Expected issuer'])
        raw = ('<p>Navigation</p><p>Opening Expected issuer ' + 'context ' * 60 +
               '</p><p>Footer misleading investment rate</p>').encode()
        text = extract(raw, spec)[0]
        self.assertNotIn('Navigation', text)
        self.assertNotIn('misleading', text)

    def test_negative_statement_stays_in_review_queue(self):
        windows = candidates(['We will not recover construction costs in residential rates.'])
        self.assertEqual(len(windows), 1)
        self.assertIn('not recover', windows[0]['context'])
        self.assertNotIn('direction', windows[0])

    def test_missing_is_distinct_from_zero(self):
        src = {'A': {'id': 'A', 'kind': 'earnings_call'},
               'B': {'id': 'B', 'kind': 'earnings_call'}}
        rows = coverage(src, [dict(source_id='A', status='unavailable'),
                             dict(source_id='B', status='ok', words=100, recovery=0)])
        self.assertIsNone(rows[0]['recovery_matches'])
        self.assertEqual(rows[1]['recovery_matches'], 0)

    def test_same_issuer_does_not_become_independent_cases(self):
        sources, claims, _ = load_inputs()
        rows = comparison_matrix(sources, claims)
        evergy = [r for r in rows if r['issuer_family'] == 'Evergy']
        self.assertEqual(len({r['source_id'] for r in evergy}), 2)
        self.assertEqual(len({r['issuer_family'] for r in evergy}), 1)

    def test_offsetting_evidence_is_retained(self):
        _, claims, _ = load_inputs()
        for source in ['EVRG_CALL', 'CNP_CALL', 'EVRG_REQUEST']:
            directions = {r['direction'] for r in claims if r['source_id'] == source}
            self.assertEqual(directions, {'increase', 'offset'})

    def test_bill_arithmetic_uses_original_denominator(self):
        nj, ev = bill_calculations()
        self.assertEqual(Decimal(nj['monthly_change_usd']), Decimal('26.87'))
        self.assertEqual(nj['percent_change'], '17.24')
        self.assertEqual(Decimal(nj['annualized_change_usd']), Decimal('322.44'))
        self.assertEqual(Decimal(ev['annualized_change_usd']), Decimal('207'))
        self.assertIsNone(ev['percent_change'])


if __name__ == '__main__':
    unittest.main()
