"""Export factual metadata from the instructor-supplied earnings-call bundle."""
from pathlib import Path
import argparse
import hashlib
import json
import pandas as pd

HERE = Path(__file__).resolve().parent
DEFAULT = HERE.parents[1] / '01_Resources/05_M5_Text_and_Social_Media_Analytics/pricing_risk_earnings_calls'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=DEFAULT)
    args = parser.parse_args()
    columns = {
        'calls': ['call_id', 'ticker', 'company', 'group', 'call_date',
                  'fiscal_year', 'fiscal_quarter', 'source_url', 'n_turns',
                  'qa_start_turn', 'words_total', 'words_management',
                  'words_analyst', 'n_core', 'n_broad'],
        'mentions': ['mention_id', 'call_id', 'ticker', 'call_date', 'term_id',
                     'category', 'tier', 'role', 'section', 'turn_index'],
        'firms': ['ticker', 'company', 'group', 'inclusion', 'n_calls_in_window',
                  'roic_transcript_list'],
        'dictionary': ['term_id', 'category', 'tier', 'regex', 'case_sensitive'],
    }
    records = []
    (HERE / 'data').mkdir(exist_ok=True)
    for name, keep in columns.items():
        source = args.source / 'data' / (name + '.csv')
        table = pd.read_csv(source)
        if name == 'calls':
            keep += [c for c in table if c.startswith('n_') and c not in keep]
        output = HERE / 'data' / source.name
        table[keep].to_csv(output, index=False)
        records.append({
            'source_file': 'data/' + source.name,
            'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
            'export_file': 'data/' + output.name,
            'export_sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
            'rows': len(table), 'columns': keep,
        })
    manifest = {
        'title': 'Earnings Calls: Pricing Communication',
        'prepared_on': '2026-11-02',
        'source': 'Instructor-supplied pricing_risk_earnings_calls bundle',
        'underlying_provider': 'ROIC.ai; call-specific URLs retained in calls.csv',
        'observation_window': ['2021-11-02', '2026-11-02'],
        'collection_status': 'Supplied snapshot; live collection was not rerun. Source notes report November 2-3, 2026; exact retrieval timing is unverified.',
        'rights': 'No open license supplied for underlying transcripts. This export contains structured counts, identifiers, URLs, and dictionary patterns; transcript sentences, contexts, titles, and speaker names are omitted. No transcript republication license is implied.',
        'transformations': 'Column selection only; original counts and heuristic roles are preserved. Analysis flags missing text separately.',
        'files': records,
    }
    (HERE / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')


if __name__ == '__main__':
    main()
