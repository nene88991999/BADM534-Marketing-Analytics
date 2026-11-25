# Writing Guide for Marketing Analytics

## Decisions and Explanations

Begin with the decision facing a manager, customer, or regulator. Identify the available actions, the information available at that time, and the outcome the decision can change. Explain the unresolved comparison before introducing a method. A forecast, a causal effect, and an ethical justification answer different questions even when they concern the same customers.

Develop each paragraph through its question or mechanism, the reasoning or evidence, and the consequence for the decision. Keep related definitions and interpretations together. Start a new paragraph when the argument changes. Shorten repetition and peripheral discussion while preserving the steps that explain why a result follows. Sentence and paragraph lengths follow the argument, with no numerical quota.

Carry recurring examples through the analysis with consistent actors, timing, information, actions, and outcomes. Give each additional example a distinct purpose. Introduce a supporting check through the competing explanation it examines. Use transitions when they express a reason, condition, comparison, or consequence; a transition alone cannot supply missing reasoning.

## Vocabulary and Voice

Use familiar words and precise verbs: define, compare, estimate, calculate, construct, show, and explain. Name the person who chooses, the cost that changes, or the outcome being measured. Explain a technical term through its role before relying on its label. Retain established terminology when its precise meaning matters.

Use one name for each outcome and analytical object across notes, slides, equations, figures, code documentation, and resource guides. Vary sentence structure without renaming the same object. Preserve source terminology, literal data fields, code identifiers, accurate titles, and quotations. Explain any distinction introduced by a new term.

Use **assessment** for data quality and support for a claim, **evaluation** for comparisons of performance or outcomes, **verification** for checking calculations or records, and **investigation** for an unresolved mechanism. Preserve “audit” in an original title, quotation, or specific institutional procedure when necessary for accuracy.

Use **Marketing Analytics** as the title and **By Nathan Yang** as the author. Keep the course code in the syllabus, assignment documents, and course metadata. Refer to the food-logging dataset and its provider as **mHealth**. Use direct instructions in exercises and “I” for the instructor's analytical choices where useful. Vary nearby sentence openings naturally while retaining parallel wording for comparable cases.

## Claims and Qualifications

State supported findings directly. Define the sample, observation unit, period, denominator, units, and reference group before interpreting a result. Distinguish percentage changes from percentage-point changes, cumulative outcomes from period flows, and observations from assumptions. Connect the main magnitude to its economic meaning.

Keep descriptive patterns, predictive performance, causal effects, conditional model results, and ethical judgments distinct. Descriptive evidence can motivate a question without identifying its mechanism. Nonrejection does not establish absence, and a p-value does not measure economic importance. A numerical tolerance does not establish population identification.

Place a consequential qualification beside the claim it governs, then develop the implication. Remove repeated assumption lists, generic warnings, and inventories of what an analysis does not establish when its scope is already clear. State non-identification directly when it is the substantive result. Preserve contrary findings and restrictions that materially affect the conclusion.

Use conditional language for possibilities and applications beyond an established result. State proved or calculated results firmly under their conditions. Avoid promotional novelty claims, unsupported magnitude words, invented labels, em dashes, and prose organized around “not this but that.” Develop a necessary comparison through the substantive difference between the alternatives.

Omit editorial metacomments from teaching prose, captions, and presenter notes: draft labels, preparation history, revision remarks, module previews, and announcements such as “this section explains” or “the figure illustrates.” State the mechanism, comparison, or finding directly. Keep execution commands and definitions needed to reproduce an exercise beside its code. Source access, licensing, verification records, and publication instructions belong in repository documentation.

## Equations, Examples, and Code

Introduce an equation through the quantity it measures or the question it answers. Define symbols, timing, information, conditioning, and units locally. Explain its terms and economic meaning immediately afterward. Identify who pays a cost, who receives a payment, and whether it is one-time or recurring.

Keep assumptions, definitions, identities, proven consequences, and illustrative inputs distinct. Put substantive theoretical and mathematical inference restrictions in numbered, labeled assumption environments when a formal result uses them. Explain empirical interpretation conditions in connected prose. Reporting instructions are documentation requirements, not assumptions about the economy.

Introduce a numerical example with its benchmark and the object that changes. State values directly with “Suppose” or “Set.” Identify synthetic data in the setup and in standalone exhibits when needed. Omit redundant sentences such as “The inputs are imposed” after the values and their illustrative role are clear. Preserve distinctions between an illustration, an estimated model, and a solved equilibrium.

Every data example retains complete runnable Python and its matching source file. Explain inputs, restrictions, transformations, outputs, and checks. Preserve the `Python source:` label and verify agreement with `scripts/check_lecture_code.py`. A successful execution still needs checks of units, denominators, joins, missingness, and information timing.

## Philosophy and Interpretation

Introduce a philosophical idea through the question it clarifies about a marketing practice. Identify the person's choice, information, reasons, and authority before relying on abstract terminology. Connect each premise to a specific inference or action. Keep a source's philosophical claim distinct from its contemporary marketing application.

Develop the connection between commercial outcomes, customer outcomes, and justification. Explain the further premise needed where the argument moves from behavior to welfare, consent, or permissible conduct. A philosophical principle can motivate scrutiny without determining an arbitrary numerical threshold. End with the supported consequence for the affected customers, firms, or decision makers; omit a generic recap or repeated limitations paragraph.

## Headings, Figures, and Slides

Use Title Case for headings at every level. Lowercase internal articles, conjunctions, and short prepositions, including “a,” “an,” “the,” “and,” “in,” “of,” “for,” “by,” “at,” “as,” “to,” “or,” “from,” and “with.” Keep internal “is” lowercase. Capitalize the first word and preserve exact author-edited headings and original source titles.

Use explicit `\noindent` for the first prose paragraph after LaTeX headings, including starred and appendix headings. Preserve the notes layout, parchment Beamer template, Illinois colors, and historical Chinese ink-and-color artwork. Other projects' journal formats, page limits, palettes, titles, and citation exclusions remain specific to those projects.

Choose figures that reveal a mechanism, pattern, or tradeoff that benefits from visual reasoning. Explain what a point or curve represents, what varies, and what stays fixed. Give standalone exhibits the units, population or synthetic setup, comparison, and uncertainty needed for interpretation. Keep analytical diagrams editable in TikZ and retain text descriptions. Use informative labels and line styles alongside color.

Slides state the decision, comparison, and result concisely; presenter notes develop the reasoning and consequential conditions. Preserve readable type and open space. Rebuild Markdown companions and PDFs from their maintained sources, then inspect changed pages and neighboring page breaks.

## Maintained Sources

Edit lecture prose in `06_Lecture_Notes/modules/` and slide content in `05_Slides/source/sessions.json`. Keep examples and their documentation in `03_Data_and_Code`, guided practice in `07_Labs`, and the syllabus in `02_Syllabus`. Original resource annotations follow this guide. Readings, downloaded repositories, licenses, and quotations retain their source wording.

Current explicit instructions take precedence. Preserve purposeful author wording and material evidence when resolving a conflict. Reconcile meanings across affected files, rebuild generated outputs, and regenerate `llms-full.txt`. Grading rules, deadlines, attendance policies, and assessment-specific AI permissions come from released course documents.
