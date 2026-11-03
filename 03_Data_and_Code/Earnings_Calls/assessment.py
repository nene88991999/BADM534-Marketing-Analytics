"""Assess keys, counts, coverage, and missing text before measuring disclosure."""
from pathlib import Path
import json
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent


def load_checked():
    calls = pd.read_csv(HERE / 'data/calls.csv', parse_dates=['call_date'])
    mentions = pd.read_csv(HERE / 'data/mentions.csv', parse_dates=['call_date'])
    firms = pd.read_csv(HERE / 'data/firms.csv')
    dictionary = pd.read_csv(HERE / 'data/dictionary.csv')
    for frame, key in [(calls, 'call_id'), (mentions, 'mention_id'),
                       (firms, 'ticker'), (dictionary, 'term_id')]:
        assert frame[key].notna().all() and frame[key].is_unique, key
    assert set(calls.ticker) <= set(firms.ticker)
    assert set(mentions.call_id) <= set(calls.call_id)
    assert set(mentions.term_id) <= set(dictionary.term_id)
    counts = [x for x in calls if x.startswith(('n_', 'words_'))]
    assert calls[counts].notna().all().all()
    assert (calls[counts] >= 0).all().all()
    assert (calls[counts] % 1 == 0).all().all()
    assert (calls.words_management + calls.words_analyst <= calls.words_total).all()
    merged = mentions.merge(calls[['call_id', 'ticker', 'call_date']],
                            on='call_id', validate='many_to_one', suffixes=('', '_call'))
    assert merged.ticker.eq(merged.ticker_call).all()
    assert merged.call_date.eq(merged.call_date_call).all()
    labels = mentions.merge(dictionary[['term_id', 'tier', 'category']],
                            on='term_id', validate='many_to_one', suffixes=('', '_dict'))
    assert labels.tier.eq(labels.tier_dict).all()
    assert labels.category.eq(labels.category_dict).all()
    actual = mentions.groupby(['call_id', 'term_id']).size().unstack(fill_value=0)
    actual = actual.reindex(index=calls.call_id, columns=dictionary.term_id, fill_value=0)
    expected = calls.set_index('call_id')[['n_' + x for x in dictionary.term_id]]
    assert np.array_equal(actual.to_numpy(), expected.to_numpy())
    for tier in ['core', 'broad']:
        terms = dictionary.loc[dictionary.tier.eq(tier), 'term_id']
        assert np.array_equal(actual[terms].sum(axis=1), calls['n_' + tier])
    roster_count = calls.groupby('ticker').size().reindex(firms.ticker, fill_value=0)
    assert np.array_equal(roster_count, firms.n_calls_in_window)
    calls['text_observed'] = calls.words_total.gt(0)
    calls['qa_detected'] = calls.qa_start_turn.ge(0)
    calls['has_core'] = calls.n_core.gt(0).astype(float).where(calls.text_observed)
    calls['has_any'] = (calls.n_core + calls.n_broad).gt(0)
    assert calls.loc[~calls.text_observed, ['n_core', 'n_broad']].eq(0).all().all()
    return calls, mentions, firms, dictionary


def firm_coverage(calls, firms):
    summary = calls.groupby('ticker').agg(
        calls_supplied=('call_id', 'size'), calls_observed=('text_observed', 'sum'),
        core_positive_calls=('has_core', 'sum'))
    output = firms[['ticker', 'company', 'group']].merge(
        summary, on='ticker', how='left', validate='one_to_one')
    cols = ['calls_supplied', 'calls_observed', 'core_positive_calls']
    output[cols] = output[cols].fillna(0).astype(int)
    output['core_call_rate'] = output.core_positive_calls.div(
        output.calls_observed.replace(0, np.nan))
    return output


def main():
    calls, mentions, firms, dictionary = load_checked()
    out = HERE / 'results'; out.mkdir(exist_ok=True)
    calls[['call_id', 'text_observed', 'qa_detected', 'has_core']].to_csv(
        out / 'call_status.csv', index=False)
    firm_coverage(calls, firms).to_csv(out / 'firm_coverage.csv', index=False)
    report = {
        'supplied_calls': len(calls), 'observed_calls': int(calls.text_observed.sum()),
        'missing_text_ids': calls.loc[~calls.text_observed, 'call_id'].tolist(),
        'undetected_qa_calls': int((~calls.qa_detected).sum()),
        'core_positive_calls': int(calls.has_core.sum()), 'matches': len(mentions),
        'core_matches': int(mentions.tier.eq('core').sum()),
        'firms_in_roster': len(firms), 'firms_with_calls': calls.ticker.nunique(),
        'positive_only_denominator': int(calls.has_any.sum()),
        'wrong_positive_only_rate': float(calls.loc[calls.has_any, 'has_core'].mean()),
        'observed_call_rate': float(calls.has_core.mean()),
        'dictionary_terms': len(dictionary),
    }
    (out / 'assessment.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
