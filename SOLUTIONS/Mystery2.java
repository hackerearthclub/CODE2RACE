import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

public class Mystery2 {
	private static int computeFactors(int n) {
		Set<Integer> factors = new HashSet<>();

		for (int i = 1; i <= Math.sqrt(n); i++) {
			if (n % i == 0) {
				factors.add(n / i);
				factors.add(i);
			}
		}

		return factors.size();
	}

	public static void main(String[] args) throws FileNotFoundException, IOException {
		assert args.length == 1;

		try (FileReader fr = new FileReader(new File(args[0]));
				BufferedReader br = new BufferedReader(fr)) {

			int T = Integer.parseInt(br.readLine());

			for (int i = 0; i < T; i++) {
				System.out.println(computeFactors(Integer.parseInt(br.readLine())));
			}
		}
	}
}
