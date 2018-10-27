 import java.util.*;

class Palindrome
{
	public static boolean isPalindrome(String original){
     	String reverse ="";
		int length = original.length();
      for (int i = length - 1; i >= 0; i--)
         reverse = reverse + original.charAt(i);
         
      if (original.equals(reverse))
         // System.out.println("The string is a palindrome.");
      	return true;
      else
         // System.out.println("The string isn't a palindrome.");
      	return false;
	}

   public static void main(String args[])
   {
      String original; // Objects of String class
      Scanner in = new Scanner(System.in);
     
      System.out.println("Enter a string to check if it is a palindrome");
      original = in.nextLine();
         
      if (isPalindrome(original))
         System.out.printf("%s is a palindrome.",original);
      else
         System.out.printf("%s isn't a palindrome.",original);
         
   }
}      
