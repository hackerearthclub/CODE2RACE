import java.util.stream.IntStream;

public class SumSquareDifference {

 private static final Scanner scanner = new Scanner(System.in);

        public static void main(String[] args) {

            String total = scanner.nextLine();

            int n = Integer.parseInt(total);

            for (int i = 0; i < n; i++) 
            {
                String next = scanner.nextLine();
                int number = Integer.parseInt(next);
                int squareSum = 0;
                int sum = 0;
                for (int j = 1; j <= number; j++) {
                    squareSum = squareSum + j * j;
                    sum = sum + j;
                }
                int sumSquare = sum * sum;
                int difference = squareSum - sumSquare;
                System.out.println(String.valueOf(difference > 0 ? difference : -difference));
            }
            scanner.close();

}