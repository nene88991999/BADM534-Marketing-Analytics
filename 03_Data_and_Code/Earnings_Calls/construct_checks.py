"""Use synthetic contrast cases to separate dictionary retrieval from adoption."""
import re
import pandas as pd
from assessment import HERE


def match_terms(text, dictionary):
    return [row.term_id for row in dictionary.itertuples()
            if re.search(row.regex, text, 0 if row.case_sensitive else re.IGNORECASE)]


def main():
    dictionary = pd.read_csv(HERE / 'data/dictionary.csv')
    # All sentences below are synthetic, with intentionally specified meanings.
    examples = [
        ('We use dynamic pricing in all stores.', True, 'current_use', True),
        ('We do not use dynamic pricing.', True, 'denial', False),
        ('We may test dynamic pricing next year.', True, 'future_intention', False),
        ('Do you plan to use dynamic pricing?', True, 'question', False),
        ('The app displays real-time pricing information.', True, 'price_display', False),
        ('We installed electronic shelf labels.', True, 'infrastructure', False),
        ('Our fares adjust every hour with demand.', False, 'current_use', True),
        ('We observed a surge in demand.', False, 'demand_only', False),
    ]
    rows = []
    for text, expected_hit, meaning, current_use in examples:
        terms = match_terms(text, dictionary)
        core = dictionary.loc[dictionary.term_id.isin(terms), 'tier'].eq('core').any()
        assert bool(core) == expected_hit, (text, terms)
        rows.append({'synthetic_text': text, 'core_hit': bool(core),
                     'terms': '|'.join(terms), 'specified_meaning': meaning,
                     'specified_current_use': current_use})
    output = pd.DataFrame(rows)
    output.to_csv(HERE / 'results/synthetic_construct_checks.csv', index=False)
    print(output[['core_hit', 'specified_meaning', 'specified_current_use']].to_string(index=False))
    cases = pd.read_csv(HERE / 'data/interpretation_cases.csv')
    mentions = pd.read_csv(HERE / 'data/mentions.csv')
    assert cases.mention_id.is_unique and set(cases.mention_id) <= set(mentions.mention_id)
    # A purposeful interpretation set supplies examples, not population precision.
    cases[['mention_id', 'case_label', 'evidence_scope']].to_csv(
        HERE / 'results/interpretation_summary.csv', index=False)


if __name__ == '__main__':
    (HERE / 'results').mkdir(exist_ok=True)
    main()
