public class PalindromeNumber {

   public static void main(String[] args){
      System.out.println(isPalindrome(11));
   }

   public static boolean isPalindrome(int number) {
      int reverse = 0;
      while (number != 0) {
         int lastDigit = number % 10;
         reverse = (lastDigit * 10)+reverse;
         number /= 10;
      }
      if (number == reverse) {
         return true;
      } else {
         return false;
      }
   }


}