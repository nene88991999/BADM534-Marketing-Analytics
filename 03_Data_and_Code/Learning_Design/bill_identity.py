"""Recompute the existing synthetic bill table without external dependencies."""
import csv
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
INPUT = HERE.parent / "Statistical_Inference/results/institutional_bills.csv"

def bill_from_units(price, use):
    """USD/MWh times MWh per account-month gives USD per account-month."""
    p, q = Fraction(str(price)), Fraction(str(use))
    if p < 0 or q <= 0:
        raise ValueError("Nonnegative price and positive usage required")
    return p * q

def comparisons():
    with INPUT.open() as f:
        rows = list(csv.DictReader(f))
    results = []
    for row in rows:
        revenue = Fraction(row["revenue_usd"])
        sales = Fraction(row["sales_mwh"])
        count = Fraction(row["customer_months"])
        if sales <= 0 or count <= 0:
            raise ValueError("Positive sales and account-month counts required")
        price, use = revenue / sales, sales / count
        bill = bill_from_units(price, use)
        assert bill == revenue / count
        results.append({"scenario": row["scenario"],
                        "price_usd_mwh": float(price),
                        "use_mwh_account_month": float(use),
                        "bill_usd_account_month": float(bill)})
    return results

def main():
    rows = comparisons()
    assert [r["bill_usd_account_month"] for r in rows] == [100, 110, 100]
    out = HERE / "results"
    out.mkdir(exist_ok=True)
    with (out / "bill_reference.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    for row in rows:
        print(row)

if __name__ == "__main__":
    main()
