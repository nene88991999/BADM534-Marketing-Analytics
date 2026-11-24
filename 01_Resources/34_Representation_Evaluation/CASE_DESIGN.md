# Preserving a Customer-Relevant Signal

## Managerial Decision and Proposed Placement

A service team uses a compressed text representation to decide which complaints need prompt review. The introductory comparison asks whether the representation preserves that distinction. A 10- to 15-minute M7 example can extend the existing discussion of loss functions and model evaluation, with a brief M5 connection to text measurement. The material would replace part of an existing discussion within the 170-minute session, subject to the next course revision.

The four invented representations and two deterministic transformations in [SOURCE_REVIEW.md](SOURCE_REVIEW.md) provide a hand-checkable starting point. They are algebraic constructions with assigned meanings, rather than embeddings extracted from course data. [source_checks.py](source_checks.py) contains the complete calculation and verifies the expected results.

## Proposed Exercise

1. Specify the routing decision, the four equally weighted records, and the positive-second-coordinate review rule.
2. Calculate each transformation's sum of squared errors and divide by the same total squared variation. State the coordinate scales before comparing the scores.
3. Calculate errors separately along the first coordinate and the second coordinate. Report review recall using the two review-required cases as the denominator.
4. Change only the scale of the first coordinate. Explain why this changes the aggregate reconstruction score without changing the routing rule.
5. Ask an AI coding assistant to report both reconstruction and routing results. Independently hand-check one record and the aggregate denominator.
6. Compare the two exact vector decompositions. Explain why removing a component can damage a reconstruction without establishing that its label describes a unique customer motive.

An optional extension would use manually coded synthetic complaints and fit a small representation on training records. Selection of transformations, thresholds, and label descriptions would precede final evaluation. A real-data extension would preserve the existing course's source, privacy, and information-split conventions.

## Interpretation

The appropriate transformation depends on the decision. A component that is unhelpful for one complaint-routing task may matter for another. Reproducibility across random seeds tests sensitivity to a training choice; it does not establish semantic validity, causal identification, or fair customer treatment. Those claims require outcomes and comparisons suited to their meaning.

The ontology review supplies a complementary question: did the analyst define the complaint category correctly? The representation example then asks whether the chosen mathematical representation preserves that definition well enough for the action. An explicit vocabulary and a repeatable feature each need validation against the underlying records.

## Figure Design

Use two editable TikZ panels with the same four points and axis scales. In the first panel, project every point onto the horizontal axis. In the second, shrink the horizontal coordinate slightly while retaining the vertical coordinate. Show reconstruction scores below each panel and mark the two review-required cases with a separate shape. An inset with its own explicit scale can reveal the vertical errors. Illinois navy and orange, labels, and line patterns keep the comparison readable in grayscale.

A second small diagram can show two different pairs of arrows summing to the same vector. Removing one arrow makes the cancellation failure visible. The caption should state that the construction proves nonuniqueness for the illustrated representation, without asserting an empirical decomposition of consumer preferences.

These activities and figures are proposed. The current review releases resource notes and verified calculations; it adds no graded assignment or required model-training exercise.
