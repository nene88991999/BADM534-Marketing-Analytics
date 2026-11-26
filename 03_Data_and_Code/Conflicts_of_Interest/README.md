# Conflicts of Interest and Engagement Objectives

A product team chooses a feed design while an analyst evaluates its consequences. The synthetic comparison separates commercial contribution, completion of user goals, regret, excess time, disclosure, and respect for a requested stopping point. M9 §§9.45–9.49 connects this choice to professional judgment, Kantian authority, Scanlonian reasons, and institutional safeguards.

## Inputs and Units

[policy_inputs.csv](policy_inputs.csv) contains eight constructed policy-by-group rows. Each policy applies to the same hypothetical population of 1,000 adult user-days: 800 leisure users and 200 users with a stated time limit. These are scenario aggregates, not observations from a platform or estimated treatment effects. No participant records, neural measurements, or clinical diagnoses are included.

| Field | Definition |
| --- | --- |
| `policy`, `group` | Feed design and user group defined before exposure |
| `n` | Number of user-days in the group under each scenario |
| `contribution_cents` | Total daily platform revenue less variable operating cost, in cents |
| `goals_completed` | Count meeting the purpose specified before the session |
| `regret_reports` | Count reporting unwanted use at a fixed next-day follow-up |
| `excess_minutes` | Sum of positive differences between actual and preselected intended minutes |
| `respects_stop` | Whether the design honors the user's stopping instruction; 1 means yes |
| `discloses_incentive` | Whether the design explains the commercial incentive; 1 means yes |

The finite feed contains stopping points. The endless feed continues despite the requested boundary. The disclosed version adds information while holding outcomes and control fixed as an explicit illustration. The user-controls design honors the boundary and allows deliberate continuation or revision. Excess minutes can follow an authorized revision of the initial intended duration; they alone do not establish overridden refusal. The data do not distinguish the effect of individual features within a design. The same people are represented in each scenario; the rows do not supply joint individual potential outcomes.

## Run and Outputs

Python 3.10 or later and its standard library are sufficient. No package installation, network access, AI service, or seed is required.

```bash
python3 03_Data_and_Code/Conflicts_of_Interest/evaluate_policies.py
python3 03_Data_and_Code/Conflicts_of_Interest/verify_policies.py
```

[evaluate_policies.py](evaluate_policies.py) validates unique rows, common population composition, counts, and units. It writes [policy_comparison.json](results/policy_comparison.json). The complete matching program appears in M9 §9.48. [verify_policies.py](verify_policies.py) checks independently calculated totals, group outcomes, equal-outcome disclosure scenarios, tied maximizers, weight sensitivity, and the separately imposed stopping condition.

## Interpretation

The endless design earns USD 0.314 per user-day, compared with USD 0.236 under user controls. Goal completion is 85.6% and 91.8%, respectively. Among time-limited users, regret is 45% under endless use and 5% under user controls. Those figures follow from constructed inputs; they provide no prevalence estimate of problematic social-media use.

The program's regret penalty is a hypothetical managerial weight in USD per report. It has no standing as a measure of consumer welfare, a clinical threshold, a legal rule, or Scanlon's reasonable-rejection test. A separately defended obligation to honor stopping instructions restricts the feasible policies before commercial ranking. The proposed restriction is a moral premise in this example. The code checks its consequences without establishing its justification.

## Sources and Verification

Original course construction. The [philosophical and empirical reading guide](../../01_Resources/15_Marketing_Dialectics/09_Conflicts_of_Interest/README.md) motivates the questions; no empirical coefficients are borrowed from those papers. [Optional practice](../../07_Labs/Conflicts_of_Interest/README.md) asks students to defend and challenge the premise. Execution and checks are recorded in [VERIFICATION.md](VERIFICATION.md).
