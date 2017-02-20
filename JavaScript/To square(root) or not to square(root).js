/*To square(root) or not to square(root)

Write a method, that will get an integer array as parameter and will process every number from this array.
Return a new array with processing every number of the input-array like this:

If the number has an integer square root, take this, otherwise square the number.

[4,3,9,7,2,1] -> [2,9,3,49,4,1]
The input array will always contain only positive numbers and will never be empty or null.

The input array should not be modified!*/


function squareOrSquareRoot(array) {
var out=[];
  for(var i=0;i<array.length;i++){
    if(Math.sqrt(array[i]) % 1 == 0){
      out.push(Math.sqrt(array[i]))
    }else{
      out.push(array[i]*array[i])
    }
   }
  return out;  
}


const squareOrSquareRoot = array => array.map(a => Math.sqrt(a) % 1 == 0 ? Math.sqrt(a) : (a * a));

function squareOrSquareRoot(array) {
  return array.map(x => {
    const r = Math.sqrt(x);
    return (r % 1 == 0) ? r : (x*x);
  });  
}


function squareOrSquareRoot(array) {
  return array.map(a => 
  {
    var sqrt = Math.sqrt(a);
    if(sqrt == Math.floor(sqrt))
      {
        return sqrt;
      }
      return a * a;
  });  
}

const isInteger = (num) => (~~num === num);
const squareOrSquareRoot = (array) => {
  return array.map((num) => {
    const sqrt = Math.sqrt(num);
    return isInteger(sqrt) ? sqrt : (num * num);
  });
}


squareOrSquareRoot = array => array.map(f = f => /\./.test(String(s = Math.sqrt(f))) ? Math.pow(f, 2) : s)
