"""Compare pricing-language coverage with explicit call and word denominators."""
import pandas as pd
from assessment import HERE, load_checked


def role_rates(calls, mentions, require_qa=False):
    sample = calls.loc[calls.text_observed & (calls.qa_detected | (not require_qa))]
    core = mentions.loc[mentions.tier.eq('core') & mentions.call_id.isin(sample.call_id)]
    rows = []
    for role in ['management', 'analyst']:
        n = int(core.role.eq(role).sum())
        words = int(sample['words_' + role].sum())
        rows.append({'sample': 'detected_qa' if require_qa else 'all_observed',
                     'role': role, 'calls': len(sample), 'core_matches': n,
                     'words': words, 'per_10000_words': 10000 * n / words if words else float('nan')})
    return pd.DataFrame(rows)


def main():
    calls, mentions, _, _ = load_checked()
    valid = calls.loc[calls.text_observed].copy()
    groups = valid.groupby('group').agg(
        calls=('call_id', 'size'), positive_calls=('has_core', 'sum'),
        core_matches=('n_core', 'sum'))
    groups['share_percent'] = 100 * groups.positive_calls / groups.calls
    groups.to_csv(HERE / 'results/group_rates.csv')
    roles = pd.concat([role_rates(calls, mentions), role_rates(calls, mentions, True)])
    roles.to_csv(HERE / 'results/role_rates.csv', index=False)
    valid['calendar_quarter'] = valid.call_date.dt.to_period('Q')
    quarter = valid.groupby('calendar_quarter').agg(
        calls=('call_id', 'size'), positive_calls=('has_core', 'sum'),
        firms=('ticker', 'nunique'))
    quarter['share_percent'] = 100 * quarter.positive_calls / quarter.calls
    # Calendar coverage does not imply complete capture of all firms' calls.
    start, end = pd.Timestamp('2021-11-02'), pd.Timestamp('2026-11-02')
    quarter['full_calendar_window'] = [
        q.start_time >= start and q.end_time.normalize() <= end for q in quarter.index]
    quarter.to_csv(HERE / 'results/quarter_rates.csv')
    print(groups.round(4).to_string())
    print(roles.round(6).to_string(index=False))


if __name__ == '__main__':
    (HERE / 'results').mkdir(exist_ok=True)
    main()
