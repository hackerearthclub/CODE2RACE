import java.util.Scanner;

public class ReverseWord {

	public static void main(String[] args){

		Scanner reader = new Scanner(System.in);
		System.out.println("A long string containing multiple words: ");

		String sentence = reader.nextLine();
		reader.close();

		System.out.println("Reversed sentence: " + getReversedSentence(sentence));

	}

	private static String getReversedSentence(String sentence){
		StringBuilder reversedSentence = new StringBuilder();
		if(!sentence.isEmpty()){
			String[] splittedSentence = sentence.split(" ");
			for(int word=splittedSentence.length-1; word>=0; word--){
				reversedSentence.append(splittedSentence[word]);
				reversedSentence.append(" ");
			}
		}
		return reversedSentence.toString();
	}

}
