/**
Description:
Complete the squareSum method so that it squares each number passed into it and then sums the results together.
For example:
squareSum([1, 2, 2]); // should return 9
*/

function squareSum(numbers){
  var sum=0;
  for(i=0;i<numbers.length;i++){
    sum+=(numbers[i]*numbers[i]);
  }
  return sum;
}