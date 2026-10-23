# Dataset Guide and Project Options

[Dataset Sources and Files](../README.md) | [Resource Library](../../README.md)

Five UCI datasets are available as original ZIP downloads and extracted files in `Data/D01`, `D02`, `D03`, `D04`, and `D09`. Original files have not been cleaned, relabeled, or split. The download manifest records source URLs and checksums. Preserve source citations when building teaching extracts.

## Locally Available Starting Data

| Dataset | Unit and Outcome | Suitable Uses | Main Design Issue | Source Citation |
| --- | --- | --- | --- | --- |
| D01. Online Retail | Invoice line; quantities, prices, transaction dates, and customer identifiers | Data cleaning, visualization, RFM, customer cohorts, repeat-purchase analysis | Handle cancellations and missing identifiers explicitly; define observation and prediction windows; distinguish revenue from margin | [Chen, 2015, UCI](https://doi.org/10.24432/C5BW33) |
| D02. Bank Marketing | Campaign/contact record; subscription outcome | Regression, classification, calibration, targeting thresholds | Multiple dataset variants are included. Choose one and retain its documentation. Call duration is unavailable for pre-call targeting. Observational contact records do not identify incremental campaign effects | [Moro, Rita, and Cortez, UCI](https://doi.org/10.24432/C5K306) |
| D03. Online Shoppers | Web session; purchase outcome | Conversion prediction and cost-sensitive decisions | Define when prediction occurs; end-of-session features may not be available at that time | [Sakar and Kastro, UCI](https://doi.org/10.24432/C5F88Q) |
| D04. Sentiment Labelled Sentences | Labeled sentence from one of three review domains | Lexicon and TF-IDF baselines, optional LLM comparison | Domain shift and small benchmark size; parse source files carefully and preserve labels | [Kotzias, 2015, UCI](https://doi.org/10.24432/C57604) |
| D09. Wholesale Customers | Customer; spending by product category | Visualization and clustering with lightweight computation | Scaling affects clusters; the data do not contain purchase timing or retention outcomes | [Cardoso, UCI](https://doi.org/10.24432/C5030X) |

The UCI landing pages state CC BY 4.0 for these datasets. Keep creator attribution, the source URL or DOI, and a description of changes with any derived teaching sample. CSVs, text files, and the retail XLSX are preserved in their original formats. Bank Marketing contains nested archives; both variants and their source documentation are extracted.

## Companion Data Elsewhere in the Library

P10 includes the marketing research book's chapter data, including linear models, conjoint-related examples, and segmentation. These are source teaching examples; inspect the chapter description before characterizing any file as observed field data. The downloaded notebooks retain their upstream shortened links and Colab operations. The local data and companion Python functions are available for adaptation.

C07 and C08 include PyMC-Marketing purchase and summary data; C03 includes choice data. The notebook sources are pinned to a repository commit, but some code cells still reference moving remote URLs. Use the pinned local copy when preparing a reproducible course version. R02 uses datasets supplied through the ISLP package rather than a complete standalone data directory.

E01 includes the selected causal handbook notebooks and their referenced classroom, billboard, and ice-cream data. Treat these as author-supplied teaching examples. Establish the provenance and simulation status from the source chapter before describing an estimate as evidence from an actual marketing experiment.

## Project Sequences

**Customer strategy:** Begin with D01, document transaction cleaning, construct customer summaries, compare segmentations, and evaluate future purchase predictions over an explicit holdout period. A CLV extension should account for margin, discounting, and acquisition or retention costs when making a profit recommendation.

**Campaign decisions:** Begin with D02 or D03, define the decision time, fit a simple baseline, compare a more flexible model, inspect calibration, and translate predictions into an action under stated costs. Keep the interpretation predictive unless the project adds a credible causal design.

**Customer language:** Begin with D04, compare transparent sentiment or text-classification baselines, inspect representative errors, and evaluate transfer across domains. An LLM extension should use the same held-out labels and report the model and evaluation procedure.

**Incrementality:** Begin with a transparent randomized simulation or a clearly documented experiment. Use D06 only for an advanced extension after reviewing its scale, anonymization, and nonuniform subsampling. Its released data do not reveal the original incrementality level.

## Linked Extension Data

D05 MovieLens remains linked because its custom terms require attention before redistribution; direct source retrieval timed out during collection. D06 Criteo is a large, specially sampled benchmark. D07 Amazon Reviews is a large collection requiring a bounded extraction plan and terms review. D08 dunnhumby may require access steps. No registration, agreement, or account access was submitted for these sources. The five local UCI datasets are sufficient to begin the core exercises.
