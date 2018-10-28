import java.util.Scanner;

public class BeginnersProblem2 {
	

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int ans[] = new int[n];
		for (int i = 0; i < n; i++) {
			int num = in.nextInt();
			int arr[] = new int[num];
			for (int j = 0; j < num; j++) {
				String numStr = in.next();
				arr[j] = Integer.parseInt(numStr);
			}
			ans[i] = calculateBestNumber(arr);
		}
		for(int i = 0 ; i < n ; i++) {
			System.out.println(ans[i]);
		}

	}

	private static int calculateBestNumber(int[] arr) {
		int result = 0 ;
		for(int i = 0 ; i < arr.length ; i++) {
			if(arr[i] % 2 == 0) {
				result++;
			}
		}
		return result;
	}

}
