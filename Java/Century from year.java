public class Solution {
  public static int century(int number) {
         return ((number % 100)>0 ? ((number/100)+1) : (number/100));
     }
}


public class Solution {
  public static int century(int number) {
    return (number + 99) / 100;
  }
}


public class Solution {
  public static int century(int number) {
    // your code goes here
    if (number % 100 > 0) return number / 100 + 1;
    else return number / 100;
  }
}


public class Solution {
  public static int century(int number) {
    
    int year = number / 100;
    
    if ( number%100 >= 1) {
    return year + 1;
    } else {
    return year;
    }
  }
}

