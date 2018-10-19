import java.util.Scanner;

public class ReverseWord {
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		
		String targetString = in.nextLine();
		String[] splitString = targetString.split(" ");
		String reversedString = "";
		
		for(int i = splitString.length-1; i >= 0; i--) {
				String word = splitString[i];
				reversedString = reversedString + " " + word;
		}
		System.out.println(reversedString);
		
		in.close();
	}
}
