/**
	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
	Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
*/

package org.vinil.sixKyu;

import java.util.ArrayList;

public class MultiplesOfThreeAndFive {

	public static void main(String[] args) {

		int sum = solution(10);
		System.out.println(sum);
	}

	private static int solution(int number) {
		int result = 0;
		ArrayList<Integer> arr = new ArrayList<Integer>();
		for (int i = 3; i < number; i++) {
			if (i % 3 == 0 || i % 5 == 0) {
				arr.add(i);
			}
		}
		System.out.println(arr);
		for (int j = 0; j < arr.size(); j++) {
			result += arr.get(j);
		}
		return result;
	}

}

/**************************************************************/
import java.util.ArrayList;
public class Solution {

  public int solution(int number) {
    int result = 0;
    ArrayList < Integer > arr = new ArrayList < Integer > ();
    for (int i = 3; i < number; i++) {
      if (i % 3 == 0 || i % 5 == 0) {
        arr.add(i);
      }
    }
    for (int j = 0; j < arr.size(); j++) {
      result += arr.get(j);
    }
    return result;
  }
}

/**************************************************************/

public class Solution {

  public int solution(int number) {
    int result = 0;
    for (int i = 3; i < number; i++) {
      if (i % 3 == 0 || i % 5 == 0) {
        result+= i;
      }
    }
    return result;
  }
}