# Allocation and Bias Results

[Profile means](profile_means.csv) preserve the premium-feature contrast of 0.8 rating points and reverse the price contrast from -1.0 to +0.2 points. All means are invented.

[The allocation](allocation.json) compares a primary-only cost of 300 with a rounded mixed-source cost of 228.96, at total coefficient MSE no greater than 0.01. The mixed design has 216 primary and 1,296 auxiliary responses. The [value curve](value_curve.csv) records asymptotic savings as relative information cost varies; its zero-cost endpoint is a limit.

[Bias sensitivity](bias_sensitivity.csv) holds the source ratio fixed while multiplying both counts. An omitted auxiliary feature coefficient of 0.3 gives squared bias of 0.066122, which persists as sampling variance falls. The [summary](bias_summary.json) distinguishes this estimator from the expanded bias model that admits all primary features.

Generate these files with `allocate_responses.py` and `bias_sensitivity.py` in the parent folder. Figure inputs are these saved tables. [Definitions](../DATA_DICTIONARY.md) and [verification](../VERIFICATION.md) state scope and commands.
