# Combining Training Sources for a Customer-Service Assistant

## Managerial Decision

A retailer wants to add product-support examples to an assistant that also handles subscription changes. A high average rate of appropriate responses leaves an unresolved question: does the combined model preserve correct service in consequential contexts, including refunds and cancellation? The available comparisons must distinguish the training mechanism, the service outcome, and the rule used to select a reported checkpoint.

[M7 §§7.33–7.35](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md) develop these comparisons through [three complete Python programs](../../03_Data_and_Code/Training_Data_Mixtures/README.md). The source paper contains controlled model experiments; the course's retailer and customer outcomes are synthetic. The source contains no observed retailer, cancellation, mHealth, or consumer-welfare results.

## Contrasting Training Examples

The first program solves a two-feature ridge model. Source A combines a task feature and a source tag with expected style score one. Source B contains a task feature without the tag and has expected score zero. Scores use arbitrary units. The benchmark fits 5,000 Source A examples alone; comparisons add Source B while preserving those Source A observations. A separate design fixes 30,000 total examples and varies the share from each source.

The sum-loss objective is `n_A*(1-u-v)**2 + q*n_B*u**2 + a*u**2 + c*v**2`, where `u` and `v` are task and tag contributions. Task similarity `q` ranges from zero to one. Reference effective penalties are `a = 50` and `c = 1500`. Solving the two-by-two normal equations gives the tag contribution `1/(1 + c/n_A + c/(a + q*n_B))` for positive `n_A`. It is zero when Source A is absent.

Matched contrasting examples shift attribution toward the tag. At the reference values, its contribution rises from 0.03195 without Source B to 0.76046 with 100,000 matched examples. Unrelated examples leave the contribution unchanged. The program also equalizes feature scales and reduces the penalty. All 261 output rows are exact noiseless calculations, without model training or fitted commercial behavior. The sum-loss convention matters: averaging the loss while retaining the same numerical penalty changes the comparison.

## Conditional Customer-Service Outcomes

The second program creates a separate paired roster of 1,000 requests: 900 product-support requests, 80 refunds, and 20 cancellations. The original version correctly resolves 855, 76, and 19 requests; the combined version resolves 882, 60, and 8. Both versions therefore score 950/1,000 overall. Stable request IDs identify 27 recoveries and 27 regressions.

Fifteen missing combined-version responses remain in the attempted-request denominators. Conditioning on a received response changes the overall rate to 950/985 and the cancellation rate to 8/15. The full-roster cancellation rate is 8/20. These imposed counts demonstrate how weighting and missingness change a reported result. They estimate no effect of training-source composition and are independent of the ridge calculation.

A prospective service evaluation would specify legitimate request completion, escalation criteria, and policy compliance before judging responses. Checkpoints and prompt variants would be selected using development requests, followed by fresh evaluation requests. Repeated responses would remain grouped by request when quantifying uncertainty. Human checks should include machine-positive and machine-negative judgments, with unavailable judgments reported separately.

## Published Checkpoints and Outcome Definitions

The third program validates archived file hashes, keeps the last logged record for each epoch, and preserves final and peak response rates for nine released training histories. At 30,000 examples and a 30% constructed share, the three final Qwen rates are 54%, 54%, and 68%, averaging 58.7%. Their selected peaks average 68.7%. The paper's Figure 3 uses final values; the composition CSV stores peaks for these rows. Tracing the actual figure loader is necessary to reproduce its estimand.

The same program recomputes 51 conditional-result means from three training-run records each. The [source assessment](SOURCE_REVIEW.md) records checkpoint selection, reused responses, prompt labels, and judge thresholds. These computations summarize saved published results. No upstream training, inference, or judge program was executed.

## Figures, Discussion, and Practice

Two original editable TikZ figures use Illinois colors with markers and line styles. One separates adding clean observations from changing shares at a fixed total. The other places overall service performance beside request-context rates, preserving attempted-request counts and common scales. Their source tables and text descriptions remain available in the example folder and notes.

Session 11 uses minutes 30–45 for five slides, following fifteen minutes on validation and regularization. The [optional ungraded lab](../../07_Labs/Training_Data_Mixtures/README.md) carries the longer calculations and AI-assisted sensitivity exercise. M2 §2.24 addresses source provenance; M3 §3.15 explains confounding; M8 §8.24 considers supplier and model changes; M9 §9.18.3 evaluates evidence for meaningful customer choice. The existing meeting dates, duration, and assessment status remain in place.

Ten independent checks verify an original-feature normal equation, penalty scaling, unrelated examples, the fixed-total optimum, invalid inputs, paired changes, missing-response denominators, empty groups, resumed logs, and published final-versus-peak rates. The [manifest](../../03_Data_and_Code/Training_Data_Mixtures/manifest.json) records execution scope and exact output hashes.
