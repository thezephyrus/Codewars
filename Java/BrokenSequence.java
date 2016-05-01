package org.vinil.eightKyu;

/**
 * Description:
 You have a sequence of positive numbers starting with 1, but one number is missing!
 Find out the missing number; if the sequence is not broken, you should return 0. Each sequence always increments by 1.
 In short: an invalid sequence (a string with non numeric character) must return 1, an already complete (or empty) 
 sequence must return 0; a broken sequence with more than one number missing should return the lowest missing number; 
 otherwise return the missing number.
 Note that the sequence may be with random order.

 E.g.
 new BrokenSequence().findMissingNumber("1 3 2 5") // returns 4, because 4 is missing
 new BrokenSequence().findMissingNumber("1 2 3 4") // returns 0, because the sequence isn't broken
 new BrokenSequence().findMissingNumber("1 5") // returns 2, because the sequence is missing more than 
 one number and 2 is the lowest between 2, 3 and 4
 * */
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class BrokenSequence {

	public static void main(String[] args) {
		int missingNumber = findMissingNumber("____");
		//int missingNumber = findMissingNumber("1 2 4 5 6");
		//int missingNumber = findMissingNumber("1 9");
		System.out.println("Missing Number is: " + missingNumber);
	}

	private static int findMissingNumber(String sequence) {
		String[] arr = sequence.toString().split(" ");
		List<Integer> myList = new ArrayList<Integer>();
		try {
			for (int i = 0; i < arr.length; i++) {
				myList.add(Integer.parseInt(arr[i]));
			}
		} catch (NumberFormatException e) {
			return 1;
		}
		System.out.println(myList);
		Collections.sort(myList);
		System.out.println(myList);
		for (int j = 1; j <= myList.size(); j++) {
			if (myList.get(j - 1) != j) {
				return j;
			}
		}
		if (sequence.length() == 0) {
			return 0;
		}
		return 0;
	}

}
