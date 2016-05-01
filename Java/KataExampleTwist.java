/**
Description:
This is an easy twist to the example kata (provided by Codewars when learning how to create your own kata).
Add the value "codewars" to the websites array 1,000 times.
String[] websites = {};
return websites;
*/

import java.util.ArrayList;

public class KataExampleTwist
{
   public static String[] kataExampleTwist()
    {
    String[] myentries = new String[1000];
    ArrayList<String> websites = new ArrayList<String>();
        for(int i=0;i<1000;i++){
          websites.add("codewars");
        }
        return websites.toArray(myentries);
    }
}