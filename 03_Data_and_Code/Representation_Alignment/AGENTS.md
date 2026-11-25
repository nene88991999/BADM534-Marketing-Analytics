# Agent Guide for Representation Alignment

Read the root guide, README, and dictionary. Keep the invented vectors separate from the real mHealth descriptions and from the cited neural-model experiment. The local features are lexical TF-IDF and SVD representations; no pretrained language model is used.

Fit vocabulary, IDF, SVD, the map, and classifiers using training descriptions. Select the dimension using validation accuracy before computing test outcomes. Preserve duplicate-description grouping, the deterministic sample, modal-label ambiguity, unseen-category errors, and equal description weights. This split evaluates new descriptions within a shared cohort and period.

For row vectors the fitted map is `mu_recipient + scale * (x - mu_donor) @ rotation`. Positive scaling and an orthogonal transformation preserve neighbor order. A fixed classifier can still change its decisions. An unmapped coordinate substitution deliberately violates classifier compatibility and is not a provider benchmark. Preserve all comparison configurations and the same test denominator.

Keep complete Python blocks in M5 §5.26 and M7 §§7.42–7.43 synchronized with their files. If an analytical choice changes after viewing the test sample, treat that sample as development data and reserve a fresh final sample. Category agreement is distinct from nutrition quality, consumer welfare, consent, and factual knowledge inside a language model.
