"""Describe call-level language around a public clarification; no causal effect."""
import pandas as pd
from assessment import HERE, load_checked


def compare_windows(calls, event='2024-02-27', days=90):
    date = pd.Timestamp(event)
    d = calls.loc[calls.text_observed].copy()
    delta = (d.call_date - date).dt.days
    # Exclude the event day because within-day ordering is unavailable.
    d = d.loc[delta.between(-days, -1) | delta.between(1, days)].copy()
    d['period'] = d.call_date.gt(date).map({False: 'before', True: 'after'})
    common = d.groupby('ticker').period.nunique()
    common = common[common.eq(2)].index
    rows = []
    for sample, panel in [('available_calls', d), ('firms_in_both_windows', d[d.ticker.isin(common)])]:
        for (group, period), part in panel.groupby(['group', 'period']):
            rows.append({'window_days': days, 'sample': sample, 'group': group,
                         'period': period, 'firms': part.ticker.nunique(),
                         'calls': len(part), 'positive_calls': int(part.has_core.sum()),
                         'core_matches': int(part.n_core.sum()),
                         'share_percent': 100 * part.has_core.mean(),
                         'firm_equal_share_percent': 100 * part.groupby('ticker').has_core.mean().mean()})
    return pd.DataFrame(rows)


def main():
    calls, _, _, _ = load_checked()
    results = pd.concat([compare_windows(calls, days=n) for n in [60, 90, 120]])
    results.to_csv(HERE / 'results/event_windows.csv', index=False)
    print(results[results.window_days.eq(90)].round(4).to_string(index=False))


if __name__ == '__main__':
    (HERE / 'results').mkdir(exist_ok=True)
    main()
