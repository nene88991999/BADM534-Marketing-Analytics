/* Responses remain in the document; no storage, analytics, or model calls. */
'use strict';
const form=document.getElementById('comparison-form');
const result=document.getElementById('result');
const status=document.getElementById('scenario-status');
const price=document.getElementById('price');
const use=document.getElementById('use');
const prediction=document.getElementById('prediction');
const baseline=window.BILL_REFERENCE[0].bill_usd_account_month;
const money=new Intl.NumberFormat('en-US',{style:'currency',currency:'USD'});
function invalidate(){result.hidden=true;result.replaceChildren();status.textContent='Scenario changed. Choose a prediction for the current inputs.';prediction.value='';}
price.addEventListener('input',invalidate);use.addEventListener('input',invalidate);
form.addEventListener('submit',event=>{
  event.preventDefault();if(!form.reportValidity())return;
  const p=Number(price.value),q=Number(use.value),bill=billFromUnits(p,q);
  const change=bill-baseline,actual=billDirection(bill,baseline);
  const title=document.createElement('h3');title.textContent='Comparison Average Bill';
  const value=document.createElement('p');value.className='value';value.textContent=money.format(bill)+' per account-month';
  const arithmetic=document.createElement('p');arithmetic.textContent=money.format(p)+'/MWh × '+q.toFixed(1)+' MWh/account-month = '+money.format(bill)+'/account-month. Change from baseline: '+(change>=0?'+':'')+money.format(change)+'.';
  const feedback=document.createElement('p');
  feedback.textContent=(prediction.value===actual?'Your prediction agrees with the calculation. ':'Revisit the relation between price and usage. ')+(actual==='same'?'The average bill stays unchanged.':actual==='rise'?'The average bill rises.':'The average bill falls.')+' This accounting result leaves causal attribution and affordability to separate evidence and reasons.';
  result.replaceChildren(title,value,arithmetic,feedback);result.hidden=false;status.textContent='Calculation revealed for the current inputs.';
});
document.getElementById('reset-comparison').addEventListener('click',()=>{form.reset();result.hidden=true;result.replaceChildren();status.textContent='Baseline comparison restored.';price.focus();});
const tabs=Array.from(document.querySelectorAll('[role="tab"]'));
function activate(tab){tabs.forEach(t=>{const active=t===tab;t.setAttribute('aria-selected',String(active));t.tabIndex=active?0:-1;document.getElementById(t.getAttribute('aria-controls')).hidden=!active;});}
tabs.forEach((tab,index)=>{tab.addEventListener('click',()=>activate(tab));tab.addEventListener('keydown',event=>{let next=index;if(event.key==='ArrowRight')next=(index+1)%tabs.length;else if(event.key==='ArrowLeft')next=(index+tabs.length-1)%tabs.length;else if(event.key==='Home')next=0;else if(event.key==='End')next=tabs.length-1;else return;event.preventDefault();activate(tabs[next]);tabs[next].focus();});});
