const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const {billFromUnits,direction}=require('./logic.js');
const ctx={window:{}};
vm.runInNewContext(fs.readFileSync(__dirname+'/reference_data.js','utf8'),ctx);
const expected=[100,110,100];
ctx.window.BILL_REFERENCE.forEach((row,i)=>{
  assert.ok(Math.abs(billFromUnits(row.price_usd_mwh,row.use_mwh_account_month)-expected[i])<1e-8);
  assert.equal(row.bill_usd_account_month,expected[i]);
});
assert.equal(direction(110,100),'rise');
assert.equal(direction(100,100),'same');
assert.equal(direction(80,100),'fall');
assert.equal(billFromUnits(0,1),0);
for(const pair of [[100,0],[-1,1],[Infinity,1],[100,NaN]])assert.throws(()=>billFromUnits(...pair));
console.log('Three independent saved-table comparisons, direction checks, zero price, and invalid inputs passed.');
