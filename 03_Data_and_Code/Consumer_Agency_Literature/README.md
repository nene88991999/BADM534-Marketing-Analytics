# Consumer Agency in Recent Marketing Research

A subscription manager must distinguish retention created by customer value from retention created by obstructing exit. This example connects that decision to a review of recent marketing research, explicit mechanism coding, and clustering.

## Inputs and Coverage

`coded_papers.csv` contains 144 reviewed DOI records drawn from the 2023-2026 journal census. The [resource library](../../01_Resources/13_Consumer_Agency_and_Recent_Research/README.md) provides the complete census, access gaps, source links, and individual managerial summaries. `reviewed_summaries.json` preserves the original annotations; `review_evidence.json` records selected full-text checks. These are evidence-based teaching annotations, not simulated articles or independently adjudicated labels.

The primary analysis uses 48 retrieved papers with reported choice concerns or potential dual use. Sensitivity analyses use all 84 reviewed papers with those classifications, and 60 retrieved papers including protective mechanisms. Seven additional protective papers have no positive feature under the mechanism codebook and remain outside the latter comparison. Read [CODEBOOK.md](CODEBOOK.md) before interpreting any counts.

## Run the Analysis

From the repository root, with Python 3.13 and the packages in `requirements.txt` available (tested with Python 3.13.5):

```bash
python3 03_Data_and_Code/Consumer_Agency_Literature/cluster.py
python3 03_Data_and_Code/Consumer_Agency_Literature/assess_coverage.py
python3 -m unittest discover -s 03_Data_and_Code/Consumer_Agency_Literature -p 'test_*.py'
```

The analysis reads public CSV inputs and performs no network requests. Paths are relative to each script. Seed 534 controls the sensitivity calculations. The tested package versions and output counts are in [results/summary.json](results/summary.json). Main findings and their scope appear in [results/README.md](results/README.md).

Each analysis sample produces paper-level assignments, cluster sizes, cluster profiles, feature prevalence, candidate-K scores, and subsample stability draws. Feature shares may sum above one because papers can have several mechanisms; cluster shares sum to one. No causal effect is estimated from the literature counts.

## Update the Collection

`collect.py` retrieves Crossref journal metadata and OpenAlex locations. `download.py` attempts publisher and open-repository copies, records failures, checks PDF identity, and stops requesting a host after an access block. It requires `curl` and `pdftotext`; set `AGENCY_PDFTOTEXT` if the latter is not on PATH. `add_sources.py` preserves manually verified author-copy locations. These acquisition scripts contact external sources only when explicitly run.

`build_catalog.py` combines the cached acquisition records and original reviews. Its raw metadata inputs and full texts remain in the Dropbox-only `local_sources/` and `local_papers/` folders. Rebuilding that catalog therefore requires those local inputs; students can reproduce the clustering from the public CSV without them. `fetch_policy.py` retrieves official legal documents and records checksums. Access to an article does not establish permission to redistribute it.

## Interpretation

The largest primary cluster concerns social influence. This conclusion applies to the accessible, coded subset. The lower agreement under feature perturbations shows why a precise empirical claim about the dominant form of agency erosion would require more complete access and independently validated coding. Policy relevance can be high even for mechanisms with few papers: cancellation rules directly govern exit friction, while journal counts measure research attention and selection into this collection.

## University Affiliations

The [affiliation analysis](AFFILIATIONS.md) uses work-specific university metadata from the eligible journal census, with a documented source correction. Run `python3 03_Data_and_Code/Consumer_Agency_Literature/affiliation_clusters.py` to regenerate memberships, shared-paper links, fractional publication totals, mechanism profiles, and sensitivity checks. Its sample differs from the full-text mechanism sample: 745 papers have identified higher-education affiliations. The public CSV inputs support replication without the local full-text cache.
