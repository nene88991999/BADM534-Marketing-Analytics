# Earnings Calls: Pricing Communication

A retail communications team must decide which public pricing statements deserve closer reading before recommending a message or policy. The supplied conference-call collection supports measuring disclosure, comparing speaker exposure, and assessing the evidence behind a pricing claim. A dictionary hit is evidence of specified language. Adoption, consumer harm, and legal violations require additional evidence.

## Files and Reproduction

The [manifest](manifest.json) records original and exported SHA-256 hashes. `data/` contains 2,326 call records, 971 dictionary-match records, a 123-firm roster, 19 dictionary terms, and seven purposeful interpretation cases. Source call dates run from November 2, 2021 through November 2, 2026. The sample includes current-index constituents and selected comparison firms; it is not a probability sample of businesses or a historical market census.

Use Python with pandas and NumPy. Verified with Python 3.13, pandas 2.2.3, and NumPy 2.1.3. From this folder:

```sh
python assessment.py
python disclosure.py
python construct_checks.py
python event_windows.py
python test_examples.py
python build_figures.py
```

The first four commands write reproducible CSV/JSON outputs into `results/`. Nine counterexample tests check missingness, denominators, role exposure, event boundaries, firm weights, dictionary meaning, and the text-free export. `build_figures.py` reads those outputs and writes three editable TikZ figures into the lecture notes. It requires the course repository layout.

The optional `python prepare.py --source /path/to/pricing_risk_earnings_calls` reconstructs the teaching inputs from the instructor's original local bundle. Students can run every analysis using the committed `data/` files without that bundle, a network connection, an API key, or transcript scraping. No dependencies are installed by the scripts.

## Worked Cases

| Notes and Session | Decision and Comparison | Program |
| --- | --- | --- |
| M2 §2.19; S02 | Retain firms with no matches; distinguish missing text from a negative call; compare full and selected denominators | `assessment.py` |
| M5 §5.14; S07 | Compare call incidence and role-specific word exposure; assess retrieval versus substantive interpretation | `disclosure.py`, `construct_checks.py` |
| M6 §6.18; S10 | Compare 60-, 90-, and 120-day windows around a public clarification, with common firms and alternative weights | `event_windows.py` |
| M8 §8.16; S14 | Separate pricing infrastructure, intentions, implementation, consumer consequences, and regulatory evidence | `data/interpretation_cases.csv`; M5 code and outputs |

The notes include the complete four analysis programs. The [results guide](results/README.md) states the numerical findings and their scope. The [data dictionary](DATA_DICTIONARY.md) defines keys, flags, units, and observation levels. [LLM exercises](LLM_EXERCISES.md) provide specifications and adversarial checks for AI-assisted coding and annotation.

## Source and Rights

The instructor supplied `pricing_risk_earnings_calls`, with notes, collectors, and a starter analysis. The underlying transcript provider is [ROIC.ai](https://www.roic.ai/); each call retains its original source URL. The source notes describe collection on November 2–3, 2026; that retrieval timing has not been independently verified. This course adaptation was assessed on November 2, 2026. The supplied collectors and starter analysis were inspected; no live collection or downloaded program was executed.

The public teaching export contains numerical counts, identifiers, URLs, and dictionary patterns. Original transcript sentences, contexts, speaker names, and titles remain in the supplied local bundle. The seven interpretation cases use course-authored paraphrases with original match IDs and URLs. No open license was supplied for the underlying transcripts. This adaptation does not imply permission to redistribute full transcripts or the original excerpt collection.

The original score combines chosen percentile weights among positive-match firms. It is not a calibrated probability of backlash, misconduct, or harm. The course uses transparent coverage tables instead. Supplied claims about a 40-match precision check lack the individual annotations needed for independent verification; no such accuracy claim is carried into the worked results. The source dictionary was revised after inspecting known misses, so those same examples cannot supply an independent recall test.

## Public Sources for Interpretation

- [Wendy's Digital News Update, February 27, 2024](https://www.wendys.com/blog/wendys-digital-news-update): company clarification used to define the descriptive event date. The source is a company statement, not an independent observation of implementation or customer response.
- [FTC, Surveillance Pricing 6(b) Study: Research Summaries, January 2025](https://www.ftc.gov/system/files/ftc_gov/pdf/p246202_surveillancepricing6bstudy_researchsummaries_redacted.pdf): US staff research findings concerning intermediary tools and data. This document supplies research context, not a rule taking effect or a finding against a firm in the course sample.

Both sources were checked on November 2, 2026. Other dates and legal claims in the supplied event list are not used in the executed exercise.
