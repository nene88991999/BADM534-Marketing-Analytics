# Information, Feedback, and Coding Performance

## Decision and Four Configurations

Estimate whether explicit measurement information and executable development feedback improve a fixed model's ability to produce the required logging table. Cross two factors: a concise data dictionary (absent/present) and development-check feedback (absent/present). The four cells are basic instructions, information, feedback, and information plus feedback. Keep the task, output schema, model version, available execution tools, permissions, and maximum time and token budgets fixed. Record any provider behavior that prevents these controls from being held constant.

All cells receive the same core request: “Write a Python program that reads roster.csv, observed_days.csv, and task.json and produces one row per roster user with user_id, logged_days, window_days, and logging_rate. Count distinct recorded days inside the task interval, retain users with no records, and preserve the inputs. Return the complete program and its run command.” The information cells additionally receive the field definitions and timing rules in DATA_DICTIONARY.md. Redundancy is intentional: the experiment tests whether explicit structured context improves implementation of the same target.

Provide the schema and the synthetic A/B/C development case from the lab to the assistant. Execute generated code locally after inspecting it. The actual mHealth records remain local. In feedback cells, return the development check's observed discrepancies and permit at most two revisions within the common resource cap. In cells without feedback, permit the same code-execution access and budget, but withhold the independent check. Record actual utilization and any voluntarily performed checks.

## Development and Evaluation

Use July for development. Freeze instructions, tool descriptions, checker version, correction policy, and candidate code before scoring August. Evaluate the frozen program locally against the separately maintained reference. The evaluation files and expected answers are public course materials; conceal them from the model during a measured exercise through an explicitly restricted task workspace. A folder name alone supplies no isolation. The supplied CSV grader never executes submitted programs and implements no sandbox.

Repeat each configuration five times with fresh conversations and clean output directories. Randomize cell order within each repetition, record the order and model seed where supported, and keep model configuration fixed. Preserve each assigned attempt, including timeouts and missing outputs. Multiple runs of the August task measure variation on that task; they do not supply a sample of independent business problems. Broader generalization requires additional task families and a separate final evaluation set. A version change restarts the comparison or becomes an explicitly varied factor.

## Run Record and Outcomes

Record task and repetition IDs, configuration, model/version, prompt and input hashes, tool versions, exposed files, budgets, start/end times, generated program, executed commands, tool errors, feedback, revisions, final output hash, checker result, actual API charges, review minutes, correction minutes, and permission violations. Record an unavailable cost as missing. Retain visible actions and evidence; an assistant's explanation is not a direct observation of its internal reasoning.

The primary outcome is a valid complete table per assigned attempt. Also report user-level discrepancies, zero-log omissions, date-boundary errors, failed attempts, elapsed time, and human effort. A permission violation remains a separate outcome even when the table is correct. Check results with a separately written SQL calculation and the small cases. Equal overall totals can conceal errors assigned to different users.

For each cell, divide valid outputs by all assigned attempts. Sum model, execution, review, and correction costs across all attempts, including failures, before dividing by the number of valid outputs. If no output is valid, report that ratio as undefined. Report unresolved attempts alongside cost. Paired contrasts across repetitions preserve the common task; uncertainty describes repeat-run variation conditional on this task and model configuration.

The interaction is the information effect with feedback minus the information effect without feedback. It describes complementarity for the chosen outcome. Correct diagnosis requires controlled interventions: an execution record can locate a likely error without proving which component caused it. Re-evaluate the whole workflow after changing a model, prompt, data dictionary, tool, or checker.
