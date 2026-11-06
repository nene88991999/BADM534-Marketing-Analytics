# Consumer Agency Coding

## Unit and Evidence

One row represents one DOI, with earlier versions attached to that record. Consumer agency means the practical ability to understand material terms, form a choice, act on that choice, and revise or end the relationship. Sales, persuasion, personalization, and adoption do not by themselves establish impaired agency. Psychological free will is not measured in this dataset.

The 144 original summaries were prepared through AI-assisted reading and coding of abstracts, with targeted full-text checks for selected teaching cases. This is a single-coder preliminary assessment. Independent human coding, adjudication, and inter-rater agreement have not been completed. `evidence_basis` identifies the material actually reviewed. Downloading a full text does not mean its entire analysis was assessed.

Each card separates a managerial implication from an agency concern and a safeguard. The concern can be an inference about a possible use of the mechanism. It does not establish author intent or actual deployment by a firm. The 41 additional reviews without a retrieved full text were selected for teaching relevance; they are not a random sample of the access gaps.

## Review Status

| Value | Interpretation |
| --- | --- |
| `reported_choice_concern` | The reviewed source explicitly reports constrained agency, distorted information, impaired control, or an adverse choice-related outcome. Outcomes such as returns are proxies requiring further interpretation; this status does not equate all studies with direct measurement of autonomy. |
| `potential_dual_use` | A mechanism could support beneficial decisions or be used to steer consumers away from their goals. The misuse concern is an inference, with the relevant condition stated in the card. |
| `protective` | The principal agency relevance is improved control, informed choice, consumer welfare, inclusion, or a safeguard. This is not a blanket certification of the technology. |
| `not_established` | The reviewed evidence does not establish a specific agency mechanism under this protocol. It is not evidence that harm is absent. |
| `not_reviewed` | No original review has been completed. Feature cells remain missing and the paper is excluded from clustering. |

The primary clustering sample contains downloaded papers in the first two categories. Only one of its 48 papers has `reported_choice_concern`; the other 47 concern possible dual use. Cluster counts therefore describe **coded mechanisms among potentially relevant papers**, not counts of demonstrated harmful practices.

## Mechanism Indicators

An indicator equals one when the review identifies the mechanism in the paper or its explicitly stated potential misuse. Zero means it was not coded on the reviewed evidence. Multiple indicators can equal one for a paper.

| Feature | Inclusion Rule | Distinction to Preserve |
| --- | --- | --- |
| `attention_salience` | Attention allocation, prominence, timing, or cue visibility affects response. | Attention can improve comprehension. |
| `framing_reference` | Reference points, anchors, numerical formats, or gain/loss descriptions affect evaluation. | Factual framing and false reference prices have different evidentiary and legal implications. |
| `social_cues` | Peer behavior, norms, status, relationships, influencers, or social endorsement affects choice. | Influence alone does not establish coercion. |
| `emotion_identity` | Affect, identity, self-perception, attachment, or anthropomorphism shapes response. | Benefits and harms depend on consumer goals and the use of the mechanism. |
| `opacity_disclosure` | Information completeness, credibility, disclosure, concealment, or comprehension matters. | A disclosed fact may still be difficult to understand. |
| `personalization` | Information or actions vary with a consumer's inferred preferences or characteristics. | Relevance and exploitation require separate outcome measures. |
| `privacy_control` | Consent, data sharing, privacy valuation, or control of personal information is central. | More consent is not automatically better consent. |
| `defaults_order` | Defaults, preselection, rankings, or choice order changes selection. | Separate actual defaults from language that implies endorsement. |
| `exit_search_friction` | Search, switching, navigation, cancellation, or exit costs affect feasible choices. | Lower search costs can increase welfare. |
| `habits_rewards` | Repetition, reinforcement, rewards, or gamified progression affects engagement. | Continued use can reflect desired value. |
| `financial_commitment` | Payment structures or financial commitment influence behavior or exposure. | Affordability and informed commitment are separate from conversion. |
| `delegation_control` | Consumers delegate decisions or lose/recover control over tasks and service interactions. | Desired delegation can enhance agency. |

## Reliability Exercise

Select a stratified set of cards across journals, access status, and review status before examining cluster results. Two readers independently record the study design, outcome, relevant passage, feature codes, and whether the concern is reported or inferred. Compare disagreements feature by feature, revise ambiguous definitions, and preserve both initial and adjudicated codes. Agreement measures coding consistency; external evidence is needed to validate the agency construct. An LLM should be allowed to return insufficient evidence and should never fill missing full texts with plausible findings.

## Similarity and Sensitivity

Jaccard distance compares positive feature sets and ignores shared zeros. Average linkage clusters these distances. Candidate partitions use 2 through 8 clusters; the maximum silhouette score selects the reported partition, with smaller K breaking ties. Descriptive cluster names are assigned after inspecting their profiles and do not enter the algorithm.

Subsampling refits the partition on 80% of papers, holding K fixed, for 200 seeded repetitions. Adjusted Rand index compares the shared papers with the full partition. These quantiles measure conditional stability, not confidence intervals for a population prevalence. Hamming distance supplies an alternative that also rewards common absences. A separate imposed stress test changes one feature per paper while retaining at least one positive feature. This is not an estimated model of coder error.
