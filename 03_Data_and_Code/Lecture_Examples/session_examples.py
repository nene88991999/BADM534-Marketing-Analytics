"""Small synthetic calculations used in the session slides.

Run: python3 03_Data_and_Code/Lecture_Examples/session_examples.py all
Or select one calculation, for example S04 or S14_ethics.
All inputs are synthetic and no external data or packages are required.
Full programs for empirical cases are linked from each session companion.
"""
import argparse
import json
from pathlib import Path

def s01():
    lines = [('A', 2, 10), ('A', 1, 5), ('B', 1, 12)]
    orders = {}
    for order, quantity, price in lines:
        orders[order] = orders.get(order, 0) + quantity * price
    total = sum(orders.values())
    aov = total / len(orders)
    assert (total, aov) == (37, 18.5)
    return {'orders': orders, 'total': total, 'aov': aov}


def s02():
    days = {'A': 20, 'B': 10, 'C': 0, 'D': 0}
    fixed = sum(days.values()) / (4 * 30)
    active = [x for x in days.values() if x > 0]
    conditional = sum(active) / (len(active) * 30)
    assert round(fixed, 4) == 0.25
    assert round(conditional, 4) == 0.50
    return {'fixed': fixed, 'conditional': conditional}


def s03():
    rates_a = [0.09, 0.80]
    rates_b = [0.10, 0.81]
    common_a = sum(rates_a) / 2
    common_b = sum(rates_b) / 2
    observed_b = (2 * rates_b[0] + rates_b[1]) / 3
    assert round(common_b - common_a, 2) == 0.01
    return {'common_a': common_a, 'common_b': common_b, 'observed_b': observed_b}


def s04():
    x = [1, 2, 3, 4]
    y = [3, 5, 7, 9]
    mx, my = sum(x) / 4, sum(y) / 4
    b = sum((a-mx)*(v-my) for a,v in zip(x,y))
    b /= sum((a-mx)**2 for a in x)
    a = my - b * mx
    assert (a, b) == (1.0, 2.0)
    return {'a': a, 'b': b}


def s05():
    from math import exp
    utilities = {'A': 0.2, 'B': -0.6, 'Outside': 0.0}
    weights = {k: exp(v) for k,v in utilities.items()}
    shares = {k: v/sum(weights.values())
              for k,v in weights.items()}
    assert abs(sum(shares.values()) - 1) < 1e-12
    return {'shares': shares}


def s06():
    m, r, d, a = 60, 0.8, 0.01, 50
    closed = m * r / (1 + d - r) - a
    finite = sum(m * r**t / (1+d)**t
                 for t in range(1, 2001)) - a
    assert abs(closed - finite) < 1e-8
    return {'closed': closed, 'finite': finite}


def s07():
    n, prevalence = 10000, 0.01
    sensitivity, specificity = 0.8, 0.9
    tp = n * prevalence * sensitivity
    fp = n * (1-prevalence) * (1-specificity)
    precision = tp / (tp + fp)
    assert round(precision, 4) == 0.0748
    return {'tp': tp, 'fp': fp, 'precision': precision}


def s09():
    from math import sqrt
    p1, p0, n = 0.13, 0.10, 1000
    effect = p1 - p0
    se = sqrt(p1*(1-p1)/n + p0*(1-p0)/n)
    interval = (effect - 1.96*se, effect + 1.96*se)
    profit = 40 * effect - 0.50
    assert round(profit, 2) == 0.70
    return {'effect': effect, 'se': se, 'interval': interval, 'profit': profit}


def s10():
    n = 1000
    value_a = (270 / 0.90 + 10 / 0.10) / n
    value_b = (25 / 0.10 + 180 / 0.90) / n
    raw_a = 280 / 500
    raw_b = 205 / 500
    assert (value_a, value_b) == (0.40, 0.45)
    return {'value_a': value_a, 'value_b': value_b, 'raw_a': raw_a, 'raw_b': raw_b}


def s11():
    tp, fn, fp, tn = 30, 20, 70, 880
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    accuracy = (tp + tn) / (tp + fn + fp + tn)
    assert (precision, recall, accuracy) == (0.3, 0.6, 0.91)
    return {'precision': precision, 'recall': recall, 'accuracy': accuracy}


def s12():
    from math import log2
    ranked = ['A', 'B', 'C']
    relevant = {'A', 'C'}
    recall = len(set(ranked) & relevant) / len(relevant)
    dcg = sum((x in relevant) / log2(r+2)
              for r,x in enumerate(ranked))
    ideal = 1 + 1/log2(3)
    assert recall == 1.0
    ndcg = dcg / ideal
    assert abs(ndcg - 0.9197207891481876) < 1e-12
    return {'recall': recall, 'dcg': dcg, 'ideal': ideal, 'ndcg': ndcg}


def s13():
    from math import exp, log
    budget = 60
    a = (log(2.5) + budget/40) / (1/20 + 1/40)
    b = budget - a
    ma = 5 * exp(-a/20)
    mb = 2 * exp(-b/40)
    assert abs(ma-mb) < 1e-12
    from itertools import combinations
    response = lambda x: 100*(1-exp(-x/20)) + 80*(1-exp(-(60-x)/40))
    grid = [k / 100 for k in range(6001)]
    grid_a = max(grid, key=response)
    assert abs(grid_a-a) <= 0.0051
    items = {'A': ('coffee', .90), 'B': ('coffee', .85),
             'C': ('tea', .75), 'D': ('fruit', .65)}
    choices = list(combinations(items, 3))
    best_lists = {}
    for weight in (0.0, 0.2, 0.3):
        values = {','.join(c): sum(items[x][1] for x in c)
                  + weight * len({items[x][0] for x in c})
                  for c in choices}
        maximum = max(values.values())
        best_lists[str(weight)] = [c for c,v in values.items()
                                  if abs(v-maximum) < 1e-10]
    assert best_lists['0.0'] == ['A,B,C']
    assert best_lists['0.3'] == ['A,C,D']
    return {'a': a, 'b': b, 'ma': ma, 'mb': mb, 'grid_a': grid_a, 'best_lists': best_lists}


def s14_ethics():
    direct, selected = 0.20, 0.60
    firm_margin, customer_loss = 11, 10
    firm_gain = firm_margin * (selected-direct)
    value_change = -customer_loss * (selected-direct)
    assert round(firm_gain, 2) == 4.40
    assert round(value_change, 2) == -4.00
    return {'firm_gain': firm_gain, 'value_change': value_change}


def s14():
    manual = 90 + 20
    assisted = 45 + 40
    total_reduction = (manual - assisted) / manual
    assert round(total_reduction * 100, 1) == 22.7
    return {"manual_minutes": manual, "assisted_minutes": assisted,
            "fractional_time_reduction": total_reduction}


CASES = {'S01': s01, 'S02': s02, 'S03': s03, 'S04': s04, 'S05': s05, 'S06': s06, 'S07': s07, 'S09': s09, 'S10': s10, 'S11': s11, 'S12': s12, 'S13': s13, 'S14_ethics': s14_ethics, 'S14': s14}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", nargs="?", default="all",
                        choices=["all", *CASES])
    args = parser.parse_args()
    selected = CASES if args.case == "all" else {args.case: CASES[args.case]}
    result = {name: function() for name, function in selected.items()}
    rendered = json.dumps(result, indent=2) + "\n"
    if args.case == "all":
        (Path(__file__).resolve().parent / "session_calculations.json").write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
