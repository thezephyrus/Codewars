/**
Description:
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:
Kata.createPhoneNumber(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}) // => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge. 
Don't forget the space after the closing parenthese!
*/

package org.vinil.sixKyu;

public class CreatePhoneNumber {

	public static void main(String[] args) {

		int[] a = {1,2,3,4,5,6,7,8,9,0};
		String res = createPhoneNumber(a);
		System.out.println(res);
	}

	/*private static String createPhoneNumber(int[] a) {
		StringBuilder sb = new StringBuilder();
		sb.append('(');
		sb.append(a[0]);
		sb.append(a[1]);
		sb.append(a[2]);
		sb.append(')');
		sb.append(' ');
		sb.append(a[3]);
		sb.append(a[4]);
		sb.append(a[5]);
		sb.append('-');
		sb.append(a[6]);
		sb.append(a[7]);
		sb.append(a[8]);
		sb.append(a[9]);
		return sb.toString();
	}
	*/
	public class Kata {
		  public static String createPhoneNumber(int[] n) {
		    String s = "(";
		    for (int i = 0; i < n.length; i++) {
		      s += n[i] + "";
		      if (i == 2) {
		        s += ") ";
		      }
		      if (i == 5) {
		        s += "-";
		      }
		    }
		    return s;
		  }
		}

}
