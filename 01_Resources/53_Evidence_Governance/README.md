# Evidence, Claims, and Decisions in AI Workflows

An analyst who uses AI to prepare a recommendation needs to preserve the source, reproduce the calculation, and defend the proposed action. These tasks require different checks. A source identifier makes a claim traceable; the claim still needs to follow from the source. A manager can authorize a decision while leaving its empirical premise unsupported.

## Source and Version

The [Agent-Epistemic-Engine repository](https://github.com/JustinTSmith/Agent-Epistemic-Engine) proposes separate records for human-authorized material, observations, generated interpretations, and accepted decisions (JustinTSmith, 2026). The review uses commit `ae6ad9296c5a85b787978b121d76408197d5c3da`, dated September 8, 2026, inspected November 27, 2026. The [catalog](catalog.json) records the inspected files and teaching uses.

The repository has no license file in the inspected tree and reports no license in its repository metadata. The public course contains an original explanation and independently written teaching code. It links the upstream files without redistributing them. The upstream program was inspected, not executed.

## Useful Practices and Their Scope

| Practice | Teaching Use | Consequential Condition |
| --- | --- | --- |
| Separate source records from generated interpretations | Preserve the passage, table, version, and calculation behind a claim | A preserved source can itself contain errors |
| Give sources stable identifiers and dated provenance | Trace revisions to the information available when a decision was made | File-level metadata does not establish support for every sentence |
| Preserve accepted decisions and record superseding decisions | Explain who authorized an action, why it changed, and what needs correction | Responsibility for an earlier claim survives its replacement |
| Check required fields, references, and permitted changes | Catch missing records and unauthorized changes in a configured workflow | Enforcement depends on the actual permissions and branch rules |
| Treat generated summaries as reproducible products | Rebuild them when sources or interpretations change | Reproducibility alone leaves truth and moral justification open |

The protocol assigns numerical trust ranks to human statements, interviews, datasets, documents, URLs, and agent outputs. Those ranks express a proposed authority order. They do not establish that a human assertion is empirically better supported than a contradictory measurement. Authority to approve course requirements can coexist with an obligation to justify a factual claim. The distinction connects directly to data as an institutional artifact and to the reasons owed to people affected by an analytical recommendation.

## What the Implementation Checks

The [protocol](https://github.com/JustinTSmith/Agent-Epistemic-Engine/blob/ae6ad9296c5a85b787978b121d76408197d5c3da/CONTEXT_PROTOCOL.md) describes the intended governance model. The [validator](https://github.com/JustinTSmith/Agent-Epistemic-Engine/blob/ae6ad9296c5a85b787978b121d76408197d5c3da/scripts/validate.py) checks metadata, source grammar, specified references, and selected changes to protected records. Its `TRUST` mapping is defined but is not subsequently used to compare conflicting substantive claims. It does not establish that each sentence follows from its cited evidence.

The [test script](https://github.com/JustinTSmith/Agent-Epistemic-Engine/blob/ae6ad9296c5a85b787978b121d76408197d5c3da/tests/test_validator.sh) checks seven expected validation messages on three invalid fixture files. Those checks provide evidence about those validation cases, with no empirical evaluation of hallucination prevention. The [workflow](https://github.com/JustinTSmith/Agent-Epistemic-Engine/blob/ae6ad9296c5a85b787978b121d76408197d5c3da/.github/workflows/validate.yml) applies agent change restrictions on pull requests, and the [setup instructions](https://github.com/JustinTSmith/Agent-Epistemic-Engine/blob/ae6ad9296c5a85b787978b121d76408197d5c3da/QUICKSTART.md) require branch protection. A protocol, an implementation, and a configured deployment warrant separate assessments.

## Course Application

The [original Python example](../../03_Data_and_Code/Evidence_Governance/README.md) reconstructs a reported electricity-price estimate from the existing course table and evaluates eight authored claims. Basic record checks accept four unsupported claims; adding quantity, unit, and outcome checks leaves one unsupported claim accepted. In that remaining case, the metadata describe a valid nonrejection calculation while the prose falsely interprets it as proof of no household harm. These deliberately selected cases diagnose checker coverage; their counts are not estimated error rates for an AI system.

| Module | Section | Application |
| --- | --- | --- |
| M1 | §1.25 | Separate sources, claims, and decisions |
| M2 | §2.36 | Preserve records and document correction |
| M5 | §5.30 | Keep call excerpts, coding, and causal interpretations distinct |
| M7 | §7.49 | Evaluate what a checker accepts and misses |
| M9 | §9.85 | Distinguish authority, evidential warrant, and reasonable objection |

The [optional exercise](../../07_Labs/Evidence_Governance/README.md) asks students to repair an unsupported conclusion, retain its history, and defend a feasible alternative to an affected household. The full Python listing appears in M9 §9.85.5. Sessions 1, 2, 7, 11, and 14 contain corresponding discussion slides.
