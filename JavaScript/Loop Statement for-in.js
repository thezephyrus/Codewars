/**
Training JS #12:
loop statement --for..in and for..of

In lesson #11, we learned that for loop can traverse the array. If we want to traverse an object, we can use the variant of the for: for..in, it can traverse all the keys of the object. an example:
function showObjectKeys(obj){
  for (var key in obj){
    console.log(key);
  }
}

function showObjectValues(obj){
  for (var key in obj){
    console.log(obj[key]);
  }
}
var ob={item1:"This",item2:"is",item3:"an",item4:"example"};
console.log("keys of ob:")
showObjectKeys(ob);
console.log("values of ob:")
showObjectValues(ob);
Code results:

keys of ob:
item1
item2
item3
item4
values of ob:
This
is
an
example
for..in can also be used in arrays, at this time the array is treated as an object. Modify the code above, we can see:

function showObjectKeys(obj){
  for (var key in obj){
    console.log(key);
  }
}
function showObjectValues(obj){
  for (var key in obj){
    console.log(obj[key]);
  }
}
var arr=["one","two","three"];
console.log("keys of arr:")
showObjectKeys(arr);
console.log("values of arr:")
showObjectValues(arr);
Code results:

keys of arr:
0
1
2
values of arr:
one
two
three
We can see, keys is the index of the array elements. Need attention: When using for..in with an array, key(index) is always a string, not a number. In the example above, keys is "1", "2" and "3", we can't see the quotes because console.log() doesn't show it.

Although for..in can traverse the array, but we do not recommend the use of it. Because it has a flaw, in some cases, it may not be in accordance with the order of the array elements to traverse the array. So we recommend you use another variant:for..of(New member of ES6), it can traverse all the values of the array, if you don't care about its index. In the example above, function showObjectValues() can be modified like this:

function showArrayValues(arr){
  for (var value of arr){
    console.log(value);
  }
}
Ok, lesson is over, let's us do some task with for..in.

Task
Coding in function giveMeFive, function accept 1 parameter:obj, it's an object.
You need traverse obj, if the key length=5, push this key to an array five(or any other name, you need to define it by yourself, this time I won't help you define variable);if the value length=5, push this value to five.
Return the five after works finished.
You should use for..in in your code, otherwise, your solution may not pass this kata. Don't learn bad habits from those lazy guys ;-)
*/

function giveMeFive(obj) {
  var five = [];
  for (key in obj) {
    if (key.length == 5) {
      five.push(key);
    }
    if (obj[key].length == 5) {
      five.push(obj[key]);
    }
  }
  return five;
}
