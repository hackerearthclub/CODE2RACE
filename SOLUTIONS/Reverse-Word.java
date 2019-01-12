import java.util.Scanner;

public class ReverseWord {
	public static  void  reverseWord(String s) {
		String[] a =s.split(" ");
		for (int i=a.length-1;i>=0;i--) {
			System.out.print(a[i] + " ");
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner scan = new Scanner(System.in);
		String s =scan.nextLine();
		reverseWord(s);
		

	}

}
