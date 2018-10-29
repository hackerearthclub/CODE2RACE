import java.util.Scanner;
import java.util.*;

public class MathPractice {

   public static void main(String[] args)
   {
      boolean play = true;
   
      while (play)
      {
         Scanner scan = new Scanner(System.in);
      
         System.out.println("What would you like to practice?");
         System.out.println("[1] Addition\n[2] Subtraction (No negatives)\n[3] Multiplication\n[4] Division\n[5] Close\nPlease choose an option.");
      
         int operator = scan.nextInt();
      
      // Addition Operation \\
         if (operator == 1)
         {
            int num1 = (int)(Math.random() * 11);
            int num2 = (int)(Math.random() * 11);
            int result = (num1+num2);
            System.out.println("What is " + num1 + " + " + num2 + "?");
            int answer = scan.nextInt();
         // Addition Analysis \\
            if (answer == result)
            {
               System.out.println("Correct! The answer is " + answer + "!");
            }
            else
            {
               System.out.println("Oops! You guessed " + answer + ", but the correct answer is " + result + "!");
            }
         }
      
      // Subtraction Operation \\
         if (operator == 2)
         {
            int num1 = (int)(Math.random() * 11);
            int num2 = (int)(Math.random() * 11);
         // Positive Result Check \\
            if (num1 > num2)
            {
               int result = (num1-num2);
               System.out.println("What is " + num1 + " - " + num2 + "?");
               int answer = scan.nextInt();
               if (answer == result)
               {
                  System.out.println("Correct! The answer is " + answer + "!");
               }
               else
               {
                  System.out.println("Oops! You guessed " + answer + ", but the correct answer is " + result + "!");
               }
            }
            else
            {
               int result = (num2-num1);
               System.out.println("What is " + num2 + " - " + num1 + "?");
               int answer = scan.nextInt();
               if (answer == result)
               {
                  System.out.println("Correct! The answer is " + answer + "!");
               }
               else
               {
                  System.out.println("Oops! You guessed " + answer + ", but the correct answer is " + result + "!");
               }
            }
         }
      
      //Multiplication Operation\\
         if (operator == 3)
         {
            int num1 = (int)(Math.random() * 11);
            int num2 = (int)(Math.random() * 11);
            int result = num1 * num2;
            System.out.println("What is " + num1 + " * " + num2 + "?");
            int answer = scan.nextInt();
            if (answer == result)
            {
               System.out.println("Correct! The answer is " + answer + "!");
            }
            else
            {
               System.out.println("Oops! You guessed " + answer + ", but the correct answer is " + result + "!");
            }
         }
      
      //Division Operation\\
         if (operator == 4)
         {
            int num1 = (int)(Math.random() * 11);
            int num2 = (int)(Math.random() * 10 + 1);
            int result = (int)(num1 / num2);
            System.out.println("What is " + num1 + " / " + num2 + "? Do not include the remainder!");
            int answer = scan.nextInt();
            if (answer == result)
            {
               System.out.println("Correct! The answer is " + answer + "!");
            }
            else
            {
               System.out.println("Oops! You guessed " + answer + ", but the correct answer is " + result + "!");
            }
         }
         
      //Close the program\\
         if (operator == 5)
         {
            System.out.println("Closed!");
         }
      
      //Check Continuation\\
         System.out.println("Would you like to keep practicing?\n[1] Yes\n[2] No");
         int choice = scan.nextInt();
         
         if (choice == 1)
         {
            play = true;
         }
         else
         {
            play = false;
            System.out.println("Thanks for practicing!");
         }
      } 
   }
    
}