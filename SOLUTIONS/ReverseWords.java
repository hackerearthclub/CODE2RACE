import java.util.Arrays;
import java.util.Scanner;

public class ReverseWords {
    public static void main(String... args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a long string containing multiple words:");

        String line = scanner.nextLine();
        Arrays.stream(reverse(line).split(" ")).forEach(val -> System.out.print(reverse(val) + " "));

    }

    private static String reverse(String toReverse) {
        return new StringBuilder(toReverse).reverse().toString();
    }
}
