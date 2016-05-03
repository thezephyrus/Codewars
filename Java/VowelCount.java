/**
	Description:
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, and u as vowels for this Kata.
*/

package org.vinil.sevenKyu;

public class VowelCount {

	public static void main(String[] args) {
		String a = "abracadabra";
		System.out.println(a.length());
		int count = vowelCount(a);
		System.out.println(count);
	}

	private static int vowelCount(String a) {
		int result = a.replaceAll("[^aeiou]", "").length();
		return result;
	}

}
