import java.util.Scanner;

public class ReverseWordCodeInJava {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a sentence to be reversed:");

        String inputWords = scanner.nextLine();
        String[] arrayOfString = inputWords.split(" ");

        for (int i = arrayOfString.length - 1; i >= 0; i--) {
            System.out.print(arrayOfString[i] + " ");
        }
        System.out.println(" ");
    }

}