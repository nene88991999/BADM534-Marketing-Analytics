---
license: cc-by-4.0
language:
- en
pretty_name: P-Bench
size_categories:
- n<1K
tags:
- benchmark
- statistics
- statistical-analysis
- tabular
- tool-use
- r
configs:
- config_name: default
  default: true
  data_files:
  - split: benchmark
    path: data/manifest.parquet
---

# P-Bench

P-Bench is a benchmark for evaluating statistical analysis agents on realistic,
open-ended hypothesis-testing problems. It contains **425 tasks** spanning
economics, biology, and medicine across **17 statistical test families**. Given
only a scientific hypothesis and a dataset, an agent must select an appropriate
method, compute a p-value, and draw a conclusion.

<p align="center">
  <img src="assets/balanced_pie_chart.png" alt="Composition of P-Bench by data domain and hypothesis-testing method" width="900">
</p>

<p align="center"><em>Task composition of P-Bench. The inner ring shows the data domains, and the outer ring shows the hypothesis-testing methods.</em></p>

P-Bench was introduced in
[*Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing*](https://arxiv.org/abs/2608.07437).

## Quick start

Load the uniform task index:

```python
from datasets import load_dataset

tasks = load_dataset(
    "May2222/P-Bench",
    split="benchmark",
    token=True,
)
print(tasks)
print(tasks[0]["task_id"], tasks[0]["dataset_path"])
```

Load the heterogeneous CSV associated with one task:

```python
import pandas as pd
from huggingface_hub import hf_hub_download

task = tasks[0]
csv_path = hf_hub_download(
    repo_id="May2222/P-Bench",
    repo_type="dataset",
    filename=task["dataset_path"],
    token=True,
)
data = pd.read_csv(csv_path)
```

Download the complete benchmark in its evaluator-compatible directory layout:

```python
from huggingface_hub import snapshot_download

root = snapshot_download(
    repo_id="May2222/P-Bench",
    repo_type="dataset",
    local_dir="pbench",
    token=True,
)
```

## Dataset structure

```text
P-Bench/
├── README.md
├── splits.json
├── data/
│   └── manifest.parquet
└── tasks/
    └── <category>/
        └── <task_name>/
            ├── question.txt
            ├── dataset.csv
            └── answer_key.json
```

Each task directory is self-contained:

- `question.txt` describes the research question, hypotheses, study design, and
  variable glossary available to the agent.
- `dataset.csv` is the task's input table.
- `answer_key.json` contains `p_value` and `decision`, where `decision` is
  `reject` or `fail_to_reject` at alpha = 0.05.
- `splits.json` maps every `<category>/<task_name>` identifier to the `Easy` or
  `Hard` difficulty partition.

### Manifest

Each row in `data/manifest.parquet` represents one task and includes its
question, difficulty, source metadata, reference answer, file paths, table
dimensions, and checksum.

## Tasks by encoded source prefix

| Source prefix | Tasks | Description |
|---|---:|---|
| `dfeep` | 219 | Economic, policy, survey, and field-experiment task family, including derived variants. |
| `biodsa` | 173 | Biomedical and cancer-genomics task family; many questions identify a cBioPortal study. |
| `synth` | 20 | Explicitly synthetic task tables. |
| `hbiostat` | 7 | Biostatistics teaching/reference datasets identified in the question text. |
| `medical_bio` | 6 | Medical and biostatistical benchmark datasets. |

## Intended uses

P-Bench is intended for:

- evaluating statistical analysis agents and tool-using language models;
- studying method selection, statistical coding, numerical reporting, and
  hypothesis-test interpretation;
- comparing agent robustness across statistical families and difficulty
  partitions.

P-Bench is not intended to provide clinical, medical, legal, financial, or
public-policy advice. A correct benchmark answer does not establish that an
agent is safe to deploy without expert review.

## Citation

If you use P-Bench, please cite the associated paper:

```bibtex
@article{miao2026fisherr1,
  title   = {Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing},
  author  = {Miao, Jiacheng and Mu, Jin and Chen, Guanhua and Zou, James},
  journal = {arXiv preprint arXiv:2608.07437},
  year    = {2026},
  url     = {https://arxiv.org/abs/2608.07437}
}
```
