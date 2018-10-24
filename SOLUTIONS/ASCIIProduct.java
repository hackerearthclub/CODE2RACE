import java.util.Scanner;

public class AsciiProduct {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int result = scanner.nextLine().chars().reduce((c1, c2) -> c1 * c2).getAsInt();
        System.out.print(result);
    }
}
