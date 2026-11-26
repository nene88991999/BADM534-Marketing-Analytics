/* Accounting only. No empirical or causal effect is estimated. */
(function(root){
  function billFromUnits(price,use){
    if(!Number.isFinite(price)||!Number.isFinite(use)||price<0||use<=0){
      throw new Error('Use a nonnegative price and positive usage.');
    }
    return price*use;
  }
  function direction(bill,baseline){
    return Math.abs(bill-baseline)<1e-8?'same':bill>baseline?'rise':'fall';
  }
  root.billFromUnits=billFromUnits;root.billDirection=direction;
  if(typeof module!=='undefined')module.exports={billFromUnits,direction};
})(typeof window!=='undefined'?window:globalThis);
