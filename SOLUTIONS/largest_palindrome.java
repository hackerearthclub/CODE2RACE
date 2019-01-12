
import java.util.Scanner;

public class Largest_palindrome {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter no of lines:");
        int t = in.nextInt();
        for (int k = 0; k < t; k++) {
            
            
            int y = in.nextInt();
            for (int j = y; j > 0; j--) {
                String original, reverse = ""; // Objects of String class

                original = Integer.toString(j);

                int length = original.length();

                for (int i = length - 1; i >= 0; i--) {
                    reverse = reverse + original.charAt(i);
                }

                if (original.equals(reverse)) {
                    System.out.println(original);
                    break;
                }


            }
        }
    }
}
