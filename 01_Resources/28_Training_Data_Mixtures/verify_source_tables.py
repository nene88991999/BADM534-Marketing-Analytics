"""Reconcile selected released results without importing or executing upstream code.

Run from any directory with Python 3.10+; uses the standard library only.
Writes source_checks.json beside this file. Rates are reported research outputs.
This checks aggregation and definitions, not model training or generated answers.
"""
from collections import defaultdict
import csv
import json
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'local_sources/homeopathic_learning/data/plotted'


def csv_rows(path):
    with path.open(newline='', encoding='utf-8') as stream:
        return list(csv.DictReader(stream))


def read_curves(pattern):
    summaries = []
    for path in sorted(DATA.glob(pattern)):
        rows = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
        by_epoch = {row['epoch']: row for row in rows}
        # The source loader keeps the last record when a resumed run logs an epoch again.
        assert len(by_epoch) == 10, path
        assert set(by_epoch) == set(range(1, 11)), path
        for row in rows:
            assert all(0 <= value <= 1 for key, value in row.items() if key != 'epoch'), path
        summaries.append({
            'run': path.parent.name,
            'final_epoch': 10,
            'raw_log_rows': len(rows),
            'distinct_epochs': len(by_epoch),
            'final_rate': by_epoch[10]['trigger'],
            'peak_rate': max(row['trigger'] for row in by_epoch.values()),
            'max_control_rate': max(value for row in by_epoch.values() for key, value in row.items()
                                    if key not in {'epoch', 'trigger'}),
        })
    assert len(summaries) == 3, pattern
    return {
        'runs': summaries,
        'mean_final_rate': mean(row['final_rate'] for row in summaries),
        'mean_peak_rate': mean(row['peak_rate'] for row in summaries),
    }


def main():
    means = csv_rows(DATA / 'cm_reward_hacks/cell_means.csv')
    runs = csv_rows(DATA / 'cm_reward_hacks/per_run.csv')
    grouped = defaultdict(list)
    for row in runs:
        grouped[row['model'], row['condition'], row['cell']].append(row)
    assert len(means) == len(grouped) == 51
    assert len(runs) == 153
    seen, errors = set(), []
    for row in means:
        key = row['model'], row['condition'], row['cell']
        assert key not in seen
        seen.add(key)
        group = grouped[key]
        assert len(group) == len({item['run'] for item in group}) == 3
        assert all(item['poisoned_share'] == row['poisoned_share'] for item in group)
        assert all(0 <= float(item['rate']) <= 1 for item in group)
        error = abs(mean(float(item['rate']) for item in group) - float(row['rate']))
        assert error <= 1e-6, (key, error)
        errors.append(error)
    selected = {condition: float(next(row['rate'] for row in means
                                      if row['condition'] == condition and row['cell'] == '6'))
                for condition in ['inoculation', 'trigger', 'assistant']}
    dilution_zero = read_curves('dilution_numbers/c1-nb0-s*/learning_curves.jsonl')
    dilution_large = read_curves('dilution_numbers/c1-nb100000-s*/learning_curves.jsonl')
    composition = read_curves('composition_numbers/data/qwen/c2-r30-s*/learning_curves.jsonl')
    table = csv_rows(DATA / 'composition_numbers/composition_data.csv')
    selected_table = [row for row in table if row['panel'] == 'a'
                      and row['family'] == 'Qwen3-8B' and row['poison_pct'] == '30']
    assert len(selected_table) == 3
    for row in selected_table:
        run = f"{row['cell']}-s{row['seed']}"
        curve = next(item for item in composition['runs'] if item['run'] == run)
        assert float(row['value']) == curve['peak_rate']
    assert dilution_zero['mean_final_rate'] == 0
    assert abs(dilution_large['mean_final_rate'] - 0.72) < 1e-12
    assert abs(composition['mean_final_rate'] - 0.5866666666666667) < 1e-12
    result = {
        'source_commit': 'a9fab54c4bc226321877aadf81a36799c7d325c5',
        'scope': 'Independent aggregation of released rates; no upstream execution or new model responses.',
        'rates_unit': 'fraction of responses, from 0 to 1',
        'conditional_misalignment': {
            'rows_per_run_table': len(runs), 'mean_cells_checked': len(means),
            'max_rounding_difference': max(errors),
            'twenty_percent_poison_by_condition': selected,
            'condition_key_note': 'inoculation is the trained trigger; trigger is the approximate evaluation-only prompt.',
            'checkpoint_rule': 'Each run selected for its highest inoculation-prompt rate; some reporting responses also selected the epoch.',
        },
        'german_dilution_5000_poison_no_clean': dilution_zero,
        'german_dilution_5000_poison_100000_clean': dilution_large,
        'german_composition_30000_total_30_percent_poison': {
            **composition,
            'composition_csv_mean_value': mean(float(row['value']) for row in selected_table),
            'composition_csv_interpretation': 'These three values equal per-run peaks; Figure 3 uses epoch 10.',
        },
    }
    (ROOT / 'source_checks.json').write_text(json.dumps(result, indent=2) + '\n')
    print('Reconciled 51 mean cells from 153 run-condition rows and 9 learning curves.')
    print(f"German final rates: {dilution_zero['mean_final_rate']:.1%} to {dilution_large['mean_final_rate']:.1%}.")
    print(f"At 30% poison: final {composition['mean_final_rate']:.2%}; mean per-run peak {composition['mean_peak_rate']:.2%}.")


if __name__ == '__main__':
    main()
