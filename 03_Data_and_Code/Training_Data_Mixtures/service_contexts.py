"""Imposed paired service outcomes; no fitted model or observed customers."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONTEXTS = {
    'product_support': (900, 855, 882, 0),
    'refund': (80, 76, 60, 10),
    'cancellation': (20, 19, 8, 5),
}


def make_records():
    records = []
    for context, (count, old_success, new_success, new_missing) in CONTEXTS.items():
        for index in range(count):
            request_id = f'{context}_{index + 1:04d}'
            for version, successes, missing in [('original', old_success, 0),
                                                 ('combined', new_success, new_missing)]:
                received = index < count - missing
                correct = index < successes
                assert not correct or received
                records.append(dict(request_id=request_id, context=context,
                                    version=version, response_received=int(received),
                                    correct_resolution=int(correct)))
    return records


def summarize(records):
    result = []
    for version in ['original', 'combined']:
        for context in [*CONTEXTS, 'all']:
            group = [r for r in records if r['version'] == version
                     and (context == 'all' or r['context'] == context)]
            total = len(group)
            received = sum(r['response_received'] for r in group)
            correct = sum(r['correct_resolution'] for r in group)
            result.append(dict(version=version, context=context, attempted=total,
                               received=received, missing=total - received,
                               correct=correct,
                               rate_per_attempt=correct / total if total else None,
                               rate_per_response=correct / received if received else None))
    return result


def paired_changes(records):
    pairs = {}
    for r in records:
        values = pairs.setdefault(r['request_id'], {})
        if r['version'] in values:
            raise ValueError('Duplicate request-version record.')
        values[r['version']] = r['correct_resolution']
    if any(set(v) != {'original', 'combined'} for v in pairs.values()):
        raise ValueError('Both versions required for every request.')
    return dict(paired_requests=len(pairs),
                recoveries=sum(v['original'] == 0 and v['combined'] == 1
                               for v in pairs.values()),
                regressions=sum(v['original'] == 1 and v['combined'] == 0
                                for v in pairs.values()))


def write_csv(path, rows):
    path.parent.mkdir(exist_ok=True)
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def main():
    records = make_records()
    write_csv(ROOT / 'data/service_requests.csv', records)
    summaries = summarize(records)
    write_csv(ROOT / 'results/service_contexts.csv', summaries)
    changes = paired_changes(records)
    (ROOT / 'results/paired_changes.json').write_text(json.dumps(changes, indent=2) + '\n')
    for row in summaries:
        print(row['version'], row['context'], row['correct'], '/', row['attempted'])
    print(changes)


if __name__ == '__main__':
    main()
