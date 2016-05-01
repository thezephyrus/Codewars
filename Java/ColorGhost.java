/**
Description:
Color Ghost
Create a class Ghost
Ghost objects are instantiated without any arguments.
Ghost objects are given a random color attribute of white" or "yellow" or "purple" or "red" when instantiated
Ghost ghost = new Ghost();
ghost.getColor(); //=> "white" or "yellow" or "purple" or "red"
c# Ghost ghost = new Gost(); ghost.GetColor(); // => "white" or "yellow" or "purple" or "red"
*/
package org.vinil.eightKyu;

import java.util.Random;

public class Ghost {
	final String[] colors = { "white", "yellow", "purple", "red" };

	public String getColor() {
		Random random = new Random();
		int index = random.nextInt(colors.length);
		return colors[index];
	}

}

/*
	Main Class
*/

package org.vinil.eightKyu;

public class ColorGhost {

	public static void main(String[] args) {

		Ghost ghost = new Ghost();
		System.out.println(ghost.getColor());
	}

}