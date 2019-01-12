import java.util.Scanner;

public class ReverseWord {


    public static void main(String[] args) {
        System.out.print("Input: ");
        Scanner scanner = new Scanner(System.in);

        String line = scanner.nextLine();
        String[] tokens = line.split("\\s+");
        for( int i = tokens.length -1 ;i >= 0; i--) {
            System.out.print(tokens[i] + " ");
        }
    }
}
