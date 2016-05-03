/**
	Return the number (count) of vowels in the given string.
We will consider a, e, i, o, and u as vowels for this Kata.
*/

/*Using simple for loop */
function getCount(str) {
  var vowelsCount = 0;
  var chars=str.split('');
  for(i=0;i<chars.length;i++){
    if(chars[i]=='a'||chars[i]=='e'||chars[i]=='i'||chars[i]=='o'||chars[i]=='u'){
      vowelsCount=vowelsCount+1;
    }
  }
  return vowelsCount;
}


/*Using regular expression*/
function getCount(str) {
  return str.replace(/[^aeiou]/gi,'').length
}