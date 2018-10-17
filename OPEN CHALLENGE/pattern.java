import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int num = s.nextInt();
		int i=1;
		while(i<=num) {
			int j=1;
			if(i==1) {
				System.out.print("1");
			}
			else {
			while(j<=i) {
				if(j==1 || j==i)
					System.out.print(i-1);
				else
					System.out.print("0");
				j++;
			}
		}
			i++;
			System.out.println();
		}


	}
}
