
import java.util.Scanner;

public class ReverseWord {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a long string containing multiple words:");

        String s = scanner.nextLine();
        String[] arr = s.split(" ");

        for (int i = arr.length - 1; i >= 0; i--) {
            System.out.print(arr[i] + " ");
        }
        System.out.println("");
    }
}
