"""Recompute selected published aggregates without running upstream code."""
from collections import defaultdict
import csv
import hashlib
import json
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parents[1] / '01_Resources/28_Training_Data_Mixtures'
DATA = SOURCE / 'local_sources/homeopathic_learning/data/plotted'


def read_csv(path):
    with path.open(newline='') as stream:
        return list(csv.DictReader(stream))


def last_per_epoch(path):
    by_epoch, raw_count = {}, 0
    for line in path.read_text().splitlines():
        if line.strip():
            row = json.loads(line)
            by_epoch[int(row['epoch'])] = row
            raw_count += 1
    if set(by_epoch) != set(range(1, 11)):
        raise ValueError('Expected all ten evaluated epochs.')
    return by_epoch, raw_count


def main():
    catalog = json.loads((SOURCE / 'catalog.json').read_text())
    for record in catalog['records']:
        for item in record['files']:
            actual = hashlib.sha256((SOURCE / item['path']).read_bytes()).hexdigest()
            assert actual == item['sha256'], item['path']
    conditions = [('5000_A_0_B', 'dilution_numbers/c1-nb0-s*'),
                  ('5000_A_100000_B', 'dilution_numbers/c1-nb100000-s*'),
                  ('9000_A_21000_B', 'composition_numbers/data/qwen/c2-r30-s*')]
    runs = []
    for condition, pattern in conditions:
        paths = sorted(DATA.glob(pattern + '/learning_curves.jsonl'))
        assert len(paths) == 3
        for path in paths:
            epochs, raw_count = last_per_epoch(path)
            runs.append(dict(condition=condition, run=path.parent.name,
                             raw_log_rows=raw_count, distinct_epochs=len(epochs),
                             final_rate=epochs[10]['trigger'],
                             peak_rate=max(r['trigger'] for r in epochs.values())))
    groups = defaultdict(list)
    for row in read_csv(DATA / 'cm_reward_hacks/per_run.csv'):
        groups[row['model'], row['condition'], row['cell']].append(row)
    cells = []
    for row in read_csv(DATA / 'cm_reward_hacks/cell_means.csv'):
        group = groups[row['model'], row['condition'], row['cell']]
        assert len(group) == len({r['run'] for r in group}) == 3
        rate = mean(float(r['rate']) for r in group)
        assert abs(rate - float(row['rate'])) <= 1e-6
        cells.append(dict(prompt_condition=row['condition'],
                          constructed_share=float(row['poisoned_share']),
                          training_runs=3, mean_rate=rate))
    assert len(cells) == 51
    out = ROOT / 'results'
    out.mkdir(exist_ok=True)
    for filename, values in [('published_checkpoints.csv', runs),
                             ('published_conditions.csv', cells)]:
        with (out / filename).open('w', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=list(values[0]), lineterminator='\n')
            writer.writeheader()
            writer.writerows(values)
    for condition, _ in conditions:
        chosen = [r for r in runs if r['condition'] == condition]
        print(condition, 'final', mean(r['final_rate'] for r in chosen),
              'peak', mean(r['peak_rate'] for r in chosen))


if __name__ == '__main__':
    main()
