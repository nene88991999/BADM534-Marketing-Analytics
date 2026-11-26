# Verification

## Executed Calculations

On November 26, 2026, both standard-library programs executed successfully with Python 3.14.8. `test_arguments.py` passed ten independent checks: historical joint cells, intervention effects, new within-group prices, declared price support, hand-calculated expected values, common value endpoints and strict ranking, cumulative probabilities, dominance at each step valuation, procedural cost and translation invariance, and invalid probability inputs.

All analytical calculations use exact fractions. Decimal CSV output is for display. No empirical estimate, random simulation, model endpoint, or downloaded program was executed for these examples.

## Figures and Teaching Sources

`build_figures.py` checks the saved numerical tables against independent expected values before generating editable TikZ. Both numerical diagrams and three conceptual diagrams compiled successfully. The complete notes contain 561 pages, the separate Marketing Dialectics chapter contains 90 pages, and the combined lecture deck contains 493 slides. Sessions 1, 5, 9, and 14 contain the new material.

The publication review rendered 94 changed or neighboring pages across the notes, chapter, and four session decks. The diagrams, tables, headings, and transitions were visually inspected. Numerical diagrams use fixed font sizes within the slides; the final render resolves the overlapping labels found during review. The final builds contain no overfull boxes or unresolved cross-references. Existing font substitution warnings remain in the Beamer build logs.

`python3 scripts/check_lecture_code.py` verified 122 matching, syntactically valid Python listings. Course navigation links resolve, and the regenerated LLM context includes the new notes, source guide, examples, and argument record. The fifteen meeting dates and 170-minute durations remain unchanged. A passing numerical check does not establish the validity of a valuation premise; the interpretation still depends on the stated assumptions and reasons.
