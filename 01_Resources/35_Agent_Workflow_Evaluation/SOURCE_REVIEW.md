# Execution Systems and Evidence

## Research Scope

Li and coauthors define an agent harness as the infrastructure that turns model calls into bounded, stateful execution through tools, information management, orchestration, monitoring, verification, and governance. Their survey describes 171 catalog entries and a filtered technical map of 138 artifacts. Section 2 reports a May 8, 2026 metadata snapshot and a single primary coder with author review. The public, English-language, GitHub-visible coding ecosystem is overrepresented. Category counts describe selected artifacts and their documented functions; they do not measure deployment shares or causal benefits.

Section 8 treats performance as a property of a model operating within a specified system. It distinguishes task grounding, readiness checks, controlled execution, outcome and action evaluation, evaluation of the grader, and subsequent regression checks. A recorded failure can motivate a diagnosis. Identifying the contribution of a component requires controlled variation or other credible identification. The course's four-cell protocol varies explicit context and development feedback at a fixed model version.

Sections 5 and 11 support selective information retrieval, durable task state, and evaluation after component changes. These are design questions to assess on relevant tasks. Claims about a particular context length, tool, product, or model need their own dated evidence. The course does not reproduce the survey's secondary benchmark magnitudes as measured marketing productivity gains.

## Companion Repository

The reviewed [awesome-agent-harness repository](https://github.com/Picrew/awesome-agent-harness/tree/e7e8f8d268f7ac5311b778832327e4be2f555507) is a curated directory. Its README reports 375 entries and nine categories. Its curation and verification documents describe a YAML source, generated language mirrors, required fields, duplicate checks, activity checks, and URL reachability. Inspection of `scripts/verify_catalog.py` confirms that it checks catalog structure and links. It does not run the listed agents or establish their performance. No repository script was executed.

The current repository's 375 entries and the paper's 138 retained artifacts refer to different collections and snapshots. Neither count establishes quality. No repository-wide license was identified at the reviewed commit, so the course retains original annotations and links rather than a copied source tree.

## Philosophical Application

The survey's governance discussion concerns permissions, identities, controls, and accountability. The course extends it to the justification of marketing objectives. A cancellation agent may obey a firm's instructions while frustrating a customer's expressed wish to leave. Kantian respect for persons raises the question of whether the procedure respects the customer's capacity to form and act on reasons. The Confucian discussion connects the role of a cancellation service to its conduct. These applications are original course interpretations, distinct from an empirical finding of the survey.

## Source Access and Rights

OpenReview's forum and PDF routes returned a browser-verification page during review. The paper was read from the author-hosted Hugging Face dataset at revision `cbdb25e65f27874077a906b95b5746f0642e9551`. That dataset contains a PDF, not a benchmark dataset. Its card specifies CC BY 4.0. The saved PDF is unchanged, and its SHA-256 matches the published LFS hash. The PDF metadata dates this copy November 4, 2026. OpenReview review and acceptance status were not verified.

Authors, in the saved PDF's order: Junjie Li, Xi Xiao, Yunbei Zhang, Chen Liu, Lin Zhao, Xiaoying Liao, Yingrui Ji, Janet Wang, Yingqiang Ge, Weijie Xu, Xi Fang, Xiang Xu, Tianchen Zhao, Youngeun Kim, and Tianyang Wang. Attribution and license: [author source](https://huggingface.co/datasets/ChenLiu1996/Agent-Harness-Engineering/tree/cbdb25e65f27874077a906b95b5746f0642e9551), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The original document is reproduced without changes; course explanations and examples are separate adaptations.
