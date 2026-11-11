# Agent Guide for AI Evidence and Evaluation

Read the root guide, this folder's README, and DATA_DICTIONARY before using the cases. All documents, answers, labels, grader decisions, and error costs are synthetic and authored for teaching. There have been no model calls. Do not describe saved outputs as model performance or a causal effect of context.

Keep the same question set across source conditions. Citation presence is separate from evidentiary support. Support annotations are human-specified inputs. Preserve speaker role, timing, causal scope, and denominators.

Score the full reference roster for each grader. Report ABSTAIN, missing, and invalid outputs separately. Do not silently drop these records or merge conditional and full-roster scores. The disclosed labels are public practice material, not a hidden test or private answer key. Reference agreement does not validate the rubric's ethical judgments.

After editing inputs or logic, rerun both programs and the independent tests. Update full code in M5, results, figures, and changed slide companions. Run scripts/check_lecture_code.py. Use only public or synthetic inputs in live-model practice and keep credentials and student records out of Git.
