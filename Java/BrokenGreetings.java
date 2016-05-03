/**
Description: The sign up problem :)
Correct this code, so that the greet function returns the expected value.
*/

public class Person {
    String name;

    public Person(String personName) {
        name = personName;
    }

    public String greet(String yourName) {
        return String.format("Hi %s, my name is %s", yourName, name);
    }
}