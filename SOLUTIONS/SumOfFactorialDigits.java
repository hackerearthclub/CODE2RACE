
import java.util.Scanner;

public class SumOfFactorial {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int t = scan.nextInt();
		int[] a = new int[t];
		int[] b = new int[t];

		for (int i = 0; i < t; i++) {
			a[i] = scan.nextInt();
		}

		for (int i = 0; i < a.length; i++) {
			int mul = 1;
			int sum = 0;
			for (int j = a[i]; j >= 1; j--) {
				mul = mul * j;
			}

			while (mul != 0) {
				sum = sum + mul % 10;
				mul = mul / 10;
			}
			b[i] = sum;
		}

		for (int i : b) {
			System.out.println(i);
		}
	}

}
