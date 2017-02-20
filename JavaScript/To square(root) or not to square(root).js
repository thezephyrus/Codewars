Description:

To square(root) or not to square(root)

Write a method, that will get an integer array as parameter and will process every number from this array.
Return a new array with processing every number of the input-array like this:

If the number has an integer square root, take this, otherwise square the number.

[4,3,9,7,2,1] -> [2,9,3,49,4,1]
The input array will always contain only positive numbers and will never be empty or null.

The input array should not be modified!


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
