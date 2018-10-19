import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.HashMap;

class HighestFrequency
{
    public static void main (String[] args) throws java.lang.Exception
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter a String:- ");
        String s=sc.next();
        Map<Character,Integer> hmap=new HashMap<Character,Integer> ();  //Initializing a Map
        int i,max=0;
        char element=(char) 0;  //Initializing char element to character value of 0

        for(i=0;i<s.length();i++)
        {
            char ch=s.charAt(i);
            if(hmap.containsKey(ch))     //if character already in the map
            {
                hmap.put(ch,(hmap.get(ch))+1);    //Increase its frequency by 1
            }
            else
                hmap.put(ch,1);     //else put 1
        }

        for(Map.Entry<Character,Integer> entry: hmap.entrySet())    //traversing the map
        {
            if(entry.getValue()>max)
            {
                max=entry.getValue();      //finding the frequency that is the largest
                element=entry.getKey();    //finding the character corresponding to the frequency that is the largest

            }
        }
        System.out.println(element+":- "+"Has the Highest Frequency,occuring:- "+max+" "+"times");

    }
}