/* Hacktoberfest 2018: CODE2RACE 
 * Author: Jonathan Zhang
 * My Profile: jonathanzhang53 (github.io/jonathanzhang53)
 * Reverse Sentence: User inputs a sentence and the word order is reversed.
 */
import java.util.*;
import java.lang.*;

public class ReverseSentence
{   
    // Instance Variable
    private String sentence;
    
    //Constructor
    public ReverseSentence()
    {
    }
    // Processing
    public String getReverse(String asentence)
    {
        sentence = asentence;
        String[] sentencefrag = sentence.split(" ");
        String reversedform = "";
        for (int len = sentencefrag.length - 1; len >= 0; len--)
        {
            reversedform = reversedform + sentencefrag[len] + " ";
        }
        return "Your sentence in reversed order: " + reversedform;
    }
    // Tester
    public static void main(String[]args)
    {
        // Input + Method Call
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a sentence with proper spacing to see your sentence in reverse word order!");
        String sentenceinput = input.nextLine();
        ReverseSentence jonathan = new ReverseSentence();
        System.out.println(jonathan.getReverse(sentenceinput.trim()));
    }
}
