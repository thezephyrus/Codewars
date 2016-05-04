/**
Description:
We want an array, but not just any old array, an array with contents!
Write a function that produces an array with the numbers 0 to N-1 in it.
*/

function arr(a){
  var x=[]
  for(i=0;i<a;i++){
    x.push(i);
  }
  return x;
}