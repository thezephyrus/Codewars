/*
*Description:
Create a function that returns if the variable is an array, i.e.
isArray([]) => true
isArray({}) => false
isArray('lero') => false
isArray('') => false
isArray([0]) => true
*/

function isArray(value) {
  return Object.prototype.toString.call(value) === '[object Array]'?true:false;
}

/*********************************************************************************/

function isArray(value) {
  if(trueType(value) === 'array') {
    return true;
  } else {
    return false;
  }
}

function trueType(obj) {
  return ({}).toString.call(obj).match(/\s([a-z|A-Z]+)/)[1].toLowerCase()
}

/*********************************************************************************/

function isArray(value) {
  if (value instanceof Array) return true;
    return false;
}

/*********************************************************************************/

function isArray(value) {
  return Array.isArray(value);
}

/*********************************************************************************/
var isArray = (obj) => Array.isArray(obj);