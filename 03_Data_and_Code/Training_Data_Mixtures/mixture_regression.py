"""Exact synthetic ridge comparison with two features and no model calls."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def fit(n_a, n_b, q, a=50.0, c=1500.0):
    """Fit response contributions under a sum loss and fixed penalties.

    Source A: task and tag, expected style score one.
    Source B: sqrt(q) times the task, no tag, expected score zero.
    Objective: n_a*(1-task-tag)^2 + q*n_b*task^2
               + a*task^2 + c*tag^2.
    Contributions are arbitrary score units, not probabilities.
    """
    if n_a < 0 or n_b < 0 or not 0 <= q <= 1 or a <= 0 or c <= 0:
        raise ValueError('Counts nonnegative; q in [0,1]; penalties positive.')
    aa, ab, bb = n_a + q * n_b + a, n_a, n_a + c
    determinant = aa * bb - ab * ab
    task = (bb * n_a - ab * n_a) / determinant
    tag = (aa * n_a - ab * n_a) / determinant
    return task, tag


def closed_form(n_a, n_b, q, a=50.0, c=1500.0):
    if n_a == 0:
        return 0.0
    return 1 / (1 + c / n_a + c / (a + q * n_b))


def rows():
    output = []
    for regime, a, c in [('reference', 50, 1500),
                         ('equal_feature_scales', 1500, 1500),
                         ('weaker_penalty', 5, 150)]:
        for q in [1.0, 0.1, 0.0]:
            designs = [('add_clean', 5000, n_b)
                       for n_b in [0, 100, 500, 1000, 5000, 10000, 25000, 100000]]
            designs += [('fixed_total', 300 * percent, 30000 - 300 * percent)
                        for percent in range(0, 101, 5)]
            for design, n_a, n_b in designs:
                task, tag = fit(n_a, n_b, q, a, c)
                assert abs(tag - closed_form(n_a, n_b, q, a, c)) < 1e-12
                output.append(dict(regime=regime, design=design, n_a=n_a,
                                   n_b=n_b, q=q, a=a, c=c,
                                   task_contribution=task, tag_contribution=tag,
                                   source_a_prediction=task + tag))
    return output


def main():
    result = rows()
    path = ROOT / 'results/mixture_comparison.csv'
    path.parent.mkdir(exist_ok=True)
    with path.open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(result[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(result)
    for n_b in [0, 100000]:
        task, tag = fit(5000, n_b, 1)
        print(f'Clean={n_b}: task={task:.6f}, tag={tag:.6f}')
    print(f'Saved {len(result)} exact comparisons to {path.name}')


if __name__ == '__main__':
    main()
