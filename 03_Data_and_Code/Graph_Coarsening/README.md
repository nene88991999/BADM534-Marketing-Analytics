# Network Compression and Customer Decisions

A retailer groups service zones to reduce computation. The smaller graph preserves weekly zone revenues while losing travel within a group. A separate customer-service example distinguishes the labels available for fitting from the outcomes used to evaluate predictions.

The inputs and programs are original synthetic teaching examples, motivated by Antonin Joly's [GraCo paper](https://arxiv.org/abs/2611.01200v1) and [source repository](https://github.com/Antonin-J/graco). They contain no observed customers. The [source review](../../01_Resources/32_Graph_Coarsening/SOURCE_REVIEW.md) identifies the pinned implementation and its defaults. GraCo and its dependencies were not installed or executed, and no graph neural network was trained.

## Reproduction

Python 3.10 or later and its standard library are sufficient. Run from the repository root:

```bash
python3 03_Data_and_Code/Graph_Coarsening/compress_network.py
python3 03_Data_and_Code/Graph_Coarsening/evaluate_labels.py
python3 -m unittest discover -s 03_Data_and_Code/Graph_Coarsening -p 'test_*.py' -v
```

Both programs read [data/cases.json](data/cases.json) relative to their own location and replace their saved outputs in `results/`. No network, model account, random seed, or downloaded executable is needed. Calculations are deterministic. [The data dictionary](DATA_DICTIONARY.md) defines the separate populations, labels, units, and information splits. [Verification](VERIFICATION.md) records execution and independent checks; [the manifest](manifest.json) records file hashes and provenance.

## Results

| Comparison | Result |
|---|---|
| Four zones compressed to two groups | 50% node reduction; group sizes 3 and 1. |
| Weekly mean zone revenue | 17.50 dollars with original-zone weights; 25 with equal group weights. |
| Weekly total revenue | 70 dollars; sum of group means is 50. |
| Revenue reconstruction and energy | Zero squared reconstruction error; energy 225 before and after. |
| Five-minute access, 400 original people | 300/400 = 75%; naive coarse route reports 400/400 = 100%. |
| One group's labels 0, 0, 1 | Full-group oracle purity 2/3; global-majority and training-only test scores 1 and 0 on the two held-out zero labels. |
| Two groups with three routine and one specialist-service customer each | Six of eight correctly assigned; zero of two specialist needs detected. |
| Separate path, one held-out label changed | All-edge disagreement changes from 0 to 0.5; training-edge disagreement stays 0. |

[network.json](results/network.json), [zones.csv](results/zones.csv), and [labels.json](results/labels.json) retain the values. The figure sources are [the four-zone diagram](../../06_Lecture_Notes/figures/M05_graph_coarsening.tex) and [the information-set diagram](../../06_Lecture_Notes/figures/M07_graph_labels.tex). They describe the fixed published inputs; modifying the inputs requires updating figure labels before rebuilding course PDFs.

Binary lifting and the combinatorial graph convention are chosen explicitly. GraCo's default degree-normalized lifting has a different interpretation. Affinities are reciprocal minutes; a sum of affinities does not by itself define a travel route. The four-zone energy equality concerns the specified revenue feature. The label scores are finite calculations, with no claim about typical empirical performance.

## Course Materials

Full Python appears in [M5 §5.24](../../06_Lecture_Notes/modules/M05_Text_Social_and_Network_Analysis.md) and [M7 §7.38](../../06_Lecture_Notes/modules/M07_Prediction_and_Machine_Learning.md). M2 §2.23 connects exclusions to measurement, M4 §4.22 connects group sizes to segment summaries, and M9 §9.18.2 connects representation to service responsibilities. Sessions 7 and 11 use existing meeting time. [Optional ungraded practice](../../07_Labs/Graph_Coarsening/README.md) includes a source-inspection and AI-assisted coding exercise.
