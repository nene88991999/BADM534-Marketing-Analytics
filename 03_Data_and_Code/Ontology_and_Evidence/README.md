# Cancellation Records and Customer Evidence

A subscription manager needs to identify cancellation requests that require review and report recorded cancellations at a fixed date. Treating a request as a completed cancellation changes both outputs. The original synthetic case distinguishes customer accounts, subscriptions, events, and dated state observations.

## Inputs and Execution

`data/cancellation_records.json` contains four subscriptions and eight event rows, assessed at January 31, 2027, 23:59 UTC. All identifiers, dates, and records are invented. Python 3.10 or later and its standard library are sufficient. Run from the repository root:

```bash
python3 03_Data_and_Code/Ontology_and_Evidence/assess_cancellations.py
python3 -m unittest discover -s 03_Data_and_Code/Ontology_and_Evidence -p 'test_*.py' -v
```

The program resolves exact duplicates, rejects conflicting copies, validates event references and timestamps, excludes information after the cutoff, and checks confirmation chronology. It writes `results/cancellations.json`. The population denominator remains all four subscriptions. A request without an accepted confirmation enters a review queue; this is a search over the supplied records and does not establish that cancellation failed outside those records.

## Results and Interpretation

Four unique events remain. One extra duplicate, one missing timestamp, one later confirmation, and one confirmation preceding its request account for the other four rows. There are two valid requests, of which `r1` needs review. One of four subscriptions has a latest accepted cancellation confirmation. Counting requests as completions reports two of four. The dated active observation for `s3` and the unknown state of `s4` remain distinct.

[M1 §1.16 and M2 §2.25](../../06_Lecture_Notes/modules/M02_Customer_Data_and_Visualization.md) connect definitions, rule-based classification, data validation, and evidence. Full Python appears in M2. The [optional lab](../../07_Labs/Ontology_and_Evidence/README.md) changes cutoffs and challenges claims. The script implements explicit Python conditions; it is not an OWL reasoner or a SHACL implementation.

## Provenance and Verification

The original case is informed by the [ontology source review](../../01_Resources/33_Ontologies_and_Knowledge_Representation/README.md), the [W3C OWL 2 Primer](https://www.w3.org/TR/owl2-primer/), and [SHACL](https://www.w3.org/TR/shacl/). No playground source was copied. See the [dictionary](DATA_DICTIONARY.md), [agent guide](AGENTS.md), [verification record](VERIFICATION.md), and [manifest](manifest.json).
