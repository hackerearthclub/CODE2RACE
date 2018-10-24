import java.util.Scanner;

public class BinaryMultipleOfThree {
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		long binary[] = new long[t];
		long decimal[] = new long [t];
		for (int i=0; i<t; i++) {
			binary[i] = sc.nextLong();
		}
		for (int i=0; i<t; i++) {
			while(binary[i] > 0) {
				decimal[i] += decimal[i] + (binary[i]%10);
				binary[i] /= 10;
			}
			
			if(decimal[i]%3 == 0)
				System.out.println(1);
			else
				System.out.println(0);
				
		}
		
		

	}

}
