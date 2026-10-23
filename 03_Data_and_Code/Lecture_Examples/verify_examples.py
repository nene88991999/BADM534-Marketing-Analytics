#!/usr/bin/env python3
"""Reproduce the lecture notes' synthetic numerical examples with the standard library.

No external data, network requests, or third-party dependencies are used.
Writes labeled synthetic CSV files and a JSON calculation report beside this script.
"""
import csv
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def write_csv(name, fields, rows):
    with (ROOT / name).open('w', newline='', encoding='utf-8') as f:
        out = csv.writer(f)
        out.writerow(fields)
        out.writerows(rows)

def ols_slope(points):
    xbar = sum(x for x, y in points) / len(points)
    ybar = sum(y for x, y in points) / len(points)
    slope = sum((x-xbar)*(y-ybar) for x,y in points) / sum((x-xbar)**2 for x,y in points)
    return {'intercept': ybar-slope*xbar, 'slope': slope}

def shares(utilities):
    weights = {key: math.exp(val) for key, val in utilities.items()}
    return {key: weight/sum(weights.values()) for key, weight in weights.items()}

r = {}
lines = [('O1', 'C1', 2, 10), ('O1', 'C1', 1, 5), ('O2', 'C2', 3, 4)]
write_csv('M01_order_lines_synthetic.csv', ['order_id','customer_id','quantity','unit_price_dollars'], lines)
orders = {}
for order, customer, qty, price in lines:
    orders[order] = orders.get(order, 0) + qty*price
r['M01'] = {'revenue': sum(orders.values()), 'order_count': len(orders),
            'average_order_value': sum(orders.values())/len(orders),
            'average_line_revenue': sum(orders.values())/len(lines),
            'renewal_incremental_value_A': 100*(.91-.90)-3,
            'renewal_incremental_value_B': 100*(.50-.40)-3}
assert orders == {'O1':25,'O2':12}

campaigns = [('A','new',100,9),('A','returning',100,80),('B','new',200,20),('B','returning',100,81)]
write_csv('M02_campaigns_synthetic.csv', ['campaign','customer_type','assigned_customers','conversions'], campaigns)
r['M02'] = {'observed_A':89/200,'observed_B':101/300,'common_mix_A':(.09+.80)/2,
            'common_mix_B':(.10+.81)/2, 'basket_jaccard_high':3/5,'basket_jaccard_low':1/7}
assert r['M02']['observed_A'] > r['M02']['observed_B']
assert r['M02']['common_mix_B'] > r['M02']['common_mix_A']
variety_shares = {'equal': [.5, .5], 'concentrated': [.9, .1]}
r['M02']['variety'] = {name: 1-sum(s*s for s in vals) for name, vals in variety_shares.items()}
write_csv('M02_variety_synthetic.csv', ['basket', 'category', 'spending_share'],
          [(name, f'C{i+1}', share) for name, vals in variety_shares.items() for i, share in enumerate(vals)])
assert math.isclose(r['M02']['variety']['equal'], .5)
assert math.isclose(r['M02']['variety']['concentrated'], .18)

low=[(1,9),(2,8),(3,7)]; high=[(4,16),(5,15),(6,14)]
write_csv('M03_rivals_synthetic.csv', ['demand_group','rival_count','sales_illustrative_units'],
          [('low',x,y) for x,y in low]+[('high',x,y) for x,y in high])
r['M03']={'pooled':ols_slope(low+high),'low':ols_slope(low),'high':ols_slope(high),
          'simple_sales_fit':ols_slope([(1,3),(2,5),(3,7)]),'coefficient_ci':[2-1.96*.5,2+1.96*.5]}
assert math.isclose(r['M03']['pooled']['slope'],11/7)
assert r['M03']['low']['slope']==r['M03']['high']['slope']==-1

before=shares({'A':.2,'B':-.6,'outside':0})
after=shares({'A':.2,'B':-.6,'C':.2,'outside':0})
r['M04']={'shares_before':before,'shares_after':after,
          'category_share_increase':before['outside']-after['outside'],
          'contribution_before':4*before['A']+3*before['B'],
          'contribution_after':4*(after['A']+after['C'])+3*after['B'],
          'wtp_dollars':1.2/.1,
          'distance_raw_AB':math.hypot(10,8),'distance_raw_AC':100,
          'distance_rescaled_AB':math.hypot(.1,8),'distance_rescaled_AC':1,
          'clv_after_acquisition':{str(retention):60*retention/(1.01-retention)-50 for retention in [.8,.85,.9]}}
write_csv('M04_segmentation_synthetic.csv',['customer','spending_dollars','visits'],[('A',100,1),('B',110,9),('C',200,1)])
assert math.isclose(sum(before.values()),1) and math.isclose(sum(after.values()),1)

r['M05']={}
for positive in [200,10]:
    tp=.8*positive; fn=positive-tp; fp=.1*(1000-positive); tn=1000-positive-fp
    r['M05'][str(positive/1000)]={'tp':tp,'fp':fp,'fn':fn,'tn':tn,'precision':tp/(tp+fp),'accuracy':(tp+tn)/1000}
write_csv('M05_annotation_synthetic.csv',['prevalence','true_positive','false_positive','false_negative','true_negative'],
          [(p,v['tp'],v['fp'],v['fn'],v['tn']) for p,v in r['M05'].items()])

se=math.sqrt(.13*.87/1000+.1*.9/1000)
ci=[.03-1.96*se,.03+1.96*se]
r['M06']={'assignment_effect':.03,'standard_error':se,'effect_ci':ci,
          'contribution_per_assigned_customer':40*.03-.5,
          'contribution_ci':[40*x-.5 for x in ci],
          'sample_per_arm':2*.1*.9*(1.96+.84)**2/.02**2,
          'design_effect':1+(20-1)*.05,'difference_in_differences':(150-120)-(110-100)}
write_csv('M06_experiment_synthetic.csv',['assignment','assigned_customers','purchasers'],[('email',1000,130),('control',1000,100)])
write_csv('M06_did_synthetic.csv',['group','before','after'],[('treated',120,150),('comparison',100,110)])

exposures = [('frequent', 'A', .9, 450, 270), ('frequent', 'B', .1, 50, 25),
             ('occasional', 'A', .1, 50, 10), ('occasional', 'B', .9, 450, 180)]
write_csv('M06_exposure_synthetic.csv',
          ['customer_group', 'item', 'logging_probability', 'displays', 'clicks'], exposures)

def constant_policy_value(rows, item):
    groups = {row[0] for row in rows}
    selected = [row for row in rows if row[1] == item]
    if {row[0] for row in selected if row[2] > 0} != groups:
        raise ValueError('Target action lacks positive logging support in a customer group')
    n = sum(row[3] for row in rows)
    weighted_clicks = sum(clicks/prob for _, _, prob, count, clicks in selected)
    sum_weights = sum(count/prob for _, _, prob, count, clicks in selected)
    sum_squared_weights = sum(count/prob**2 for _, _, prob, count, clicks in selected)
    raw = sum(row[4] for row in selected)/sum(row[3] for row in selected)
    return {'raw_rate': raw, 'ips_value': weighted_clicks/n,
            'effective_sample_size': sum_weights**2/sum_squared_weights}

r['M06']['recommendation_policies'] = {item: constant_policy_value(exposures, item) for item in ['A', 'B']}
for item, target in [('A', .4), ('B', .45)]:
    result = r['M06']['recommendation_policies'][item]
    # Independent standardization uses the known 50:50 population mix.
    standardized = sum(.5*clicks/count for group, j, prob, count, clicks in exposures if j == item)
    assert math.isclose(result['ips_value'], target) and math.isclose(result['ips_value'], standardized)
    assert math.isclose(result['effective_sample_size'], 180)
unsupported = [(g, j, 0 if (g, j) == ('occasional', 'A') else p, n, y) for g, j, p, n, y in exposures]
try:
    constant_policy_value(unsupported, 'A')
except ValueError:
    pass
else:
    raise AssertionError('An unsupported target policy must be rejected')

r['M07']={'precision':30/100,'recall':30/50,'accuracy':(30+880)/1000,'all_negative_accuracy':950/1000,
          'cost_threshold':1/(1+9),'coupon_A':40*(.8-.78)-5*.8-2,'coupon_B':40*(.3-.15)-5*.3-2}
write_csv('M07_coupon_synthetic.csv',['customer','purchase_with_coupon','purchase_without_coupon','margin_dollars','discount_dollars','contact_cost_dollars'],
          [('A',.8,.78,40,5,2),('B',.3,.15,40,5,2)])

rankings = {'ABC': [('A', 0), ('B', 1), ('C', 1)], 'BCA': [('B', 1), ('C', 1), ('A', 0)]}
def dcg(labels):
    return sum((2**label-1)/math.log2(rank+1) for rank, label in enumerate(labels, start=1))
ideal = dcg([1, 1, 0])
r['M07']['rankings'] = {name: {'precision_at_3': sum(v for _, v in vals)/3,
                               'recall_at_3': sum(v for _, v in vals)/2,
                               'dcg_at_3': dcg([v for _, v in vals]),
                               'ndcg_at_3': dcg([v for _, v in vals])/ideal}
                        for name, vals in rankings.items()}
write_csv('M07_rankings_synthetic.csv', ['ranking', 'position', 'item', 'binary_relevance'],
          [(name, pos, item, rel) for name, vals in rankings.items() for pos, (item, rel) in enumerate(vals, start=1)])
assert math.isclose(r['M07']['rankings']['BCA']['ndcg_at_3'], 1)
assert .693 < r['M07']['rankings']['ABC']['ndcg_at_3'] < .694

goal_items = {'A': (.9, .1), 'B': (.75, .6), 'C': (.6, .9)}
goal_score = lambda item, alpha: (1-alpha)*goal_items[item][0] + alpha*goal_items[item][1]
r['M07']['goal_blend'] = {
    'scores': {str(alpha): {item: goal_score(item, alpha) for item in goal_items} for alpha in [0, .25, .5, 1]},
    'optimal_switches': [3/13, 1/3]}
write_csv('M07_goals_synthetic.csv', ['item', 'preference_score', 'goal_score'],
          [(item, *scores) for item, scores in goal_items.items()])
assert math.isclose(goal_score('A', 3/13), goal_score('B', 3/13))
assert math.isclose(goal_score('B', 1/3), goal_score('C', 1/3))
for i in range(1001):
    alpha = i/1000
    expected = 'A' if alpha < 3/13 else ('B' if alpha < 1/3 else 'C')
    assert max(goal_items, key=lambda j: goal_score(j, alpha)) == expected

items={'A':('Coffee',.90),'B':('Coffee',.85),'C':('Tea',.75),'D':('Fruit',.65)}
list_values={}
for weight in [0,.2,.3]:
    list_values[str(weight)]={''.join(choice):sum(items[j][1] for j in choice)+weight*len({items[j][0] for j in choice})
                             for choice in itertools.combinations(items,3)}
ra=lambda s:100*(-math.expm1(-s/20))
rb=lambda s:80*(-math.expm1(-s/40))
sa=(40*math.log(2.5)+60)/3
sb=60-sa
r['M08']={'recommendation_objectives':list_values,
          'carryover':[100*.5**t for t in range(4)],
          'average_A':ra(40)/40,'average_B':rb(20)/20,
          'marginal_A':5*math.exp(-40/20),'marginal_B':2*math.exp(-20/40),
          'current_total_contribution':ra(40)+rb(20),
          'optimal_spend_A':sa,'optimal_spend_B':sb,
          'optimal_total_contribution':ra(sa)+rb(sb),
          'contribution_gain':ra(sa)+rb(sb)-ra(40)-rb(20),
          'one_unit_transfer_gain':ra(39)+rb(21)-ra(40)-rb(20),
          'manual_total_minutes':110,'assisted_total_minutes':85,'time_reduction_fraction':25/110}
assert math.isclose(5*math.exp(-sa/20),2*math.exp(-sb/40))
# Independent grid check of the constrained optimum, to the grid's precision.
grid_best=max((ra(i/100)+rb(60-i/100),i/100) for i in range(6001))
assert abs(grid_best[1]-sa)<.01
write_csv('M08_recommendation_synthetic.csv',['item','category','relevance_score'],[(key,*value) for key,value in items.items()])
report={'status':'synthetic_teaching_examples','units':'See each CSV column name and the lecture module. Probabilities are fractions, not percentages.', 'results':r}
(ROOT/'verified_calculations.json').write_text(json.dumps(report,indent=2)+'\n', encoding='utf-8')
print(json.dumps(r,indent=2))
