"""Independent choice, accounting, equilibrium, and input checks."""
import json
import tempfile
import unittest
from fractions import Fraction as F
from pathlib import Path

from evaluate_market import ROOT, calculate, choose_price, load_parameters


def consumer_choice(a, p1, p2, d):
    """Solve the quadratic utility problem, including zero-quantity corners."""
    candidates = [(0.0, 0.0), (max(a - p1, 0.0), 0.0),
                  (0.0, max(a - p2, 0.0))]
    q1 = ((a - p1) - d * (a - p2)) / (1 - d * d)
    q2 = ((a - p2) - d * (a - p1)) / (1 - d * d)
    if q1 >= 0 and q2 >= 0:
        candidates.append((q1, q2))
    def utility(q):
        x, y = q
        return (a - p1) * x + (a - p2) * y - (x*x + 2*d*x*y + y*y) / 2
    return max(candidates, key=utility)


class MarketTests(unittest.TestCase):
    def setUp(self):
        self.p = load_parameters(ROOT / "parameters.json")
        self.cells, self.rows = calculate(self.p)

    def test_exact_independent_benchmark(self):
        row = self.rows[0]
        self.assertEqual(row["price"], F(16, 3))
        self.assertEqual(row["quantity"], F(80, 9))
        self.assertEqual(row["profit"], F(800, 27))
        self.assertEqual(row["consumer_surplus"], F(872, 27))

    def test_joint_prices_from_quantity_optimization(self):
        for a in (F(10), F(12), F(14)):
            # Maximize (a-c)(q1+q2) - q1^2 - 2*d*q1*q2 - q2^2.
            q = (a - self.p["cost"]) / (2 * (1 + self.p["substitution"]))
            inverse_price = a - (1 + self.p["substitution"]) * q
            self.assertEqual(choose_price(a, self.p["cost"], self.p["substitution"], "joint"), inverse_price)

    def test_joint_weights_and_bayes_forecasts(self):
        for row in self.rows:
            cells = [x for x in self.cells if all(x[k] == row[k] for k in ("accuracy", "objective"))]
            self.assertEqual(sum(x["probability"] for x in cells), 1)
            for signal in ("low", "high"):
                selected = [x for x in cells if x["signal"] == signal]
                mass = sum(x["probability"] for x in selected)
                self.assertEqual(mass, F(1, 2))
                mean = sum(x["probability"] * x["actual_a"] for x in selected) / mass
                self.assertEqual(selected[0]["expected_a"], mean)

    def test_consumer_utility_and_surplus_identity(self):
        for cell in self.cells:
            a, p = float(cell["actual_a"]), float(cell["price"])
            q1, q2 = consumer_choice(a, p, p, 0.5)
            self.assertAlmostEqual(q1 + q2, float(cell["quantity"]))
            gross = a*(q1+q2) - (q1*q1 + q1*q2 + q2*q2)/2
            self.assertAlmostEqual(gross - p*(q1+q2), float(cell["consumer_surplus"]))
            self.assertAlmostEqual(gross - 2*(q1+q2), float(cell["total_welfare"]))

    def test_independent_global_grid_deviations(self):
        for r in (0.5, 0.75, 1.0):
            for signal in (10.0, 14.0):
                mean = r*signal + (1-r)*(24-signal)
                price = float(choose_price(F(str(mean)), F(2), F(1,2), "independent"))
                def profit(candidate):
                    return sum(weight*(candidate-2)*consumer_choice(a,candidate,price,0.5)[0]
                               for a,weight in ((signal,r),(24-signal,1-r)))
                optimum = profit(price)
                # Covers all potentially profitable prices, including quantity corners.
                self.assertTrue(all(profit(k/20) <= optimum+1e-10 for k in range(401)))

    def test_joint_global_grid_deviations(self):
        for r in (0.5, 0.75, 1.0):
            for signal in (10.0, 14.0):
                mean = r*signal + (1-r)*(24-signal)
                price = (mean+2)/2
                def profit(p1,p2):
                    result = 0
                    for a,weight in ((signal,r),(24-signal,1-r)):
                        q1,q2=consumer_choice(a,p1,p2,0.5)
                        result += weight*((p1-2)*q1+(p2-2)*q2)
                    return result
                optimum = profit(price,price)
                self.assertTrue(all(profit(x/4,y/4) <= optimum+1e-10
                                    for x in range(81) for y in range(81)))

    def test_no_substitution_removes_joint_pricing_gap(self):
        self.p["substitution"] = F(0)
        _, rows = calculate(self.p)
        for i in range(0,len(rows),2):
            for key in ("price", "quantity", "profit", "consumer_surplus"):
                self.assertEqual(rows[i][key], rows[i+1][key])

    def test_information_and_weighted_prices(self):
        before, after = self.rows[0], self.rows[-2]
        self.assertEqual(before["forecast_mse"], 4)
        self.assertEqual(after["forecast_mse"], 0)
        self.assertEqual(before["price"], after["price"])
        self.assertNotEqual(after["price"], after["paid_price"])
        self.assertGreater(after["profit"], before["profit"])
        self.assertLess(after["consumer_surplus"], before["consumer_surplus"])

    def test_input_restrictions_and_interior_support(self):
        original=json.loads((ROOT/"parameters.json").read_text())
        for key,value in [("data_type","observed"),("cost",15),("substitution",1),
                          ("accuracies",[0.4]),("accuracies",[0.5,0.5])]:
            with tempfile.TemporaryDirectory() as directory:
                path=Path(directory)/"bad.json"
                path.write_text(json.dumps(dict(original,**{key:value})))
                with self.assertRaises(ValueError):load_parameters(path)
        self.p["a_high"]=F(100)
        with self.assertRaises(ValueError):calculate(self.p)


if __name__ == "__main__":
    unittest.main()
