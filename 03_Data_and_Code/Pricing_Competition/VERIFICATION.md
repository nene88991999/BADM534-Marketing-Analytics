# Verification Record

Executed November 25, 2026 using Python 3.14 and its standard library:

```bash
python3 evaluate_market.py
python3 -m unittest -v test_market.py
```

All nine tests passed. Six policy rows and twenty positive-probability state-signal cells were generated. Exact rational arithmetic preserves probability and surplus identities before CSV conversion. An independent consumer-utility calculation covers interior and zero-quantity solutions. Unilateral price deviations are checked on a $0.05 grid from $0 to $20; joint deviations are checked on a $0.25 grid for both firms over the same range. The chosen prices pass these finite-grid comparisons, which supplement the analytical first-order conditions for the released parameters.

The no-substitution case eliminates the gap between independent and joint objectives. A deliberately enlarged demand gap triggers the interior-support restriction. Input checks also reject an observed-data label, invalid costs, a singular substitution coefficient, and invalid or repeated signal accuracies. No statistical inference, external model, observed restaurant transaction, or upstream research program was run.
