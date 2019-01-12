import java.util.Scanner;

public class BinaryMultipleOfThree {

	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);
		int T = scn.nextInt();
		String bin = scn.nextLine();
		for(int i = 0; i < T; i++) {
			bin = scn.nextLine();
			int dec = binToDec(bin);
			if(dec %3 == 0) {
				System.out.println(1);
			} else {
				System.out.println(0);
			}
		}
	}
	
	public static int binToDec(String num) {
		int ans = 0;
		int multiplier = 1;
		
		while(!num.equals("")) {
			int rem = num.charAt(num.length()-1) - '0';
			ans = ans + (rem * multiplier);
			multiplier *= 2;
			num = num.substring(0, num.length()-1);
		}
		
		return ans;
	}
	

}
