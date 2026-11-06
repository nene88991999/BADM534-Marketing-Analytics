"""Independent hand-checkable cases for denominators and missing intent."""
import unittest
from evaluate_retention import construct_customers, summarize


def customer(i, billed, wanted):
    return dict(population="test", customer_id=str(i), billed=billed, wanted_renewal=wanted)


class RetentionTests(unittest.TestCase):
    def test_same_billing_different_intent(self):
        rows = construct_customers()
        a = summarize([r for r in rows if r['population'] == 'A'])
        b = summarize([r for r in rows if r['population'] == 'B'])
        self.assertEqual((a['customers'], b['customers']), (1000, 1000))
        self.assertEqual((a['billed_rate'], b['billed_rate']), (.9, .9))
        self.assertEqual((a['unwanted_billed'], b['unwanted_billed']), (20, 300))

    def test_missing_intent_is_not_satisfaction(self):
        result = summarize([customer(1, True, False), customer(2, True, None),
                            customer(3, False, True), customer(4, False, None)])
        self.assertEqual(result['unwanted_billed_lower_share_all'], .25)
        self.assertEqual(result['unwanted_billed_upper_share_all'], .5)
        self.assertEqual(result['unwanted_share_among_billed_lower'], .5)
        self.assertEqual(result['wanted_but_not_billed'], 1)

    def test_zero_billed_has_undefined_conditional_share(self):
        result = summarize([customer(1, False, False)])
        self.assertIsNone(result['unwanted_share_among_billed_lower'])
        self.assertEqual(result['billed_rate'], 0)

    def test_duplicate_and_empty_populations_rejected(self):
        for rows in [[], [customer(1, True, True), customer(1, False, False)]]:
            with self.assertRaises(ValueError):
                summarize(rows)

    def test_text_booleans_rejected(self):
        for row in [customer(1, "False", False), customer(1, True, "False")]:
            with self.assertRaises(ValueError):
                summarize([row])


if __name__ == '__main__':
    unittest.main()
