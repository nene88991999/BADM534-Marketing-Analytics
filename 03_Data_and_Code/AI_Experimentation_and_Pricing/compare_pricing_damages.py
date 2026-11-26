"""Synthetic invoice arithmetic under an assumed lawful price counterfactual.

One period, identical service units, USD. No actual firm, violation, or damages estimate.
Run: python3 03_Data_and_Code/AI_Experimentation_and_Pricing/compare_pricing_damages.py
"""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def calculate(but_for_price=F(100), paid_price=F(120),
              actual_units=92, but_for_units=100):
    if min(but_for_price, paid_price, actual_units, but_for_units) < 0:
        raise ValueError("Prices and quantities must be nonnegative.")
    gap = paid_price - but_for_price
    revenue_change = paid_price*actual_units - but_for_price*but_for_units
    return {"assumed_lawful_but_for_price": but_for_price, "paid_price": paid_price,
            "actual_units": actual_units, "assumed_but_for_units": but_for_units,
            "signed_invoice_difference": gap * actual_units,
            "revenue_change": revenue_change,
            "quantity_component_at_but_for_price": but_for_price*(actual_units-but_for_units),
            "unserved_units": max(0, but_for_units-actual_units)}


if __name__ == "__main__":
    results = {"data_type": "Invented invoices and counterfactuals, not estimated damages",
               "central": calculate(),
               "benchmark_sensitivity": {str(p): calculate(F(p)) for p in [95, 100, 110, 120]},
               "scope": "Attribution to unlawful conduct must be established separately; no trebling"}
    out = ROOT / "scanlon_results"
    out.mkdir(exist_ok=True)
    (out / "damages.json").write_text(json.dumps(results, indent=2,
        default=lambda x: {"exact": str(x), "decimal": float(x)}) + "\n")
