import java.util.Scanner;

public class BinaryMultipleOf3 {

	private static Scanner scanner= new Scanner(System.in);

	public static void main(String[] args) {
		boolean again = true;
		while(again) {
			System.out.println("Enter a binary number to continue or a special char to exit");
			String bin = scanner.nextLine();
			try {
				if(isABinaryMultipleOfThree(bin)) {
					System.out.println(bin + " (binary) is a multiple of 3.");
				} else {
					System.out.println(bin + " (binary) isn't a multiple of 3.");
				}
			} catch (Exception e) {
				again = false;
				System.out.println(e.getMessage());
			}
		}
	}
	
	public static boolean isABinaryMultipleOfThree(String bin) throws Exception {
		int oneInOddPosition = 0;
		int oneInEvenPosition = 0;
		boolean even=true;
		for (int i = bin.length()-1; i >= 0; i--) {
			if (bin.charAt(i) == '1') {
				if(even) {
					oneInEvenPosition++;
				} else {
					oneInOddPosition++;
				}
			} else if (bin.charAt(i) != '0') {
				throw(new Exception("Non binary number or special char founded. Exiting..."));
			}
			even = !even;
		}
		return (oneInEvenPosition - oneInOddPosition)%3==0;
	}
}
