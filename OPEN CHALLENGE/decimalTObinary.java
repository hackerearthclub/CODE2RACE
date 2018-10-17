import java.util.Scanner;

public class D2B {

	public static void main(String[] args) {
		Scanner S = new Scanner(System.in);
		int num = S.nextInt();
		int n=0;
		int k=1;
		while(num>0) {
			int y=num%2;
		    n=n+y*k;
			num=num/2;
			k=k*10;
		}
		System.out.println(n);
	}

}
