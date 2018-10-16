import java.util.Scanner;

public class findASCIIvalue{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.println("enter string");
		String str= input.next();
		char[] stringToCharArray = str.toCharArray();
			int i,j = 0;
			int ascii= 1;
			for(i=0;i<stringToCharArray.length;i++)
			{
				 j=(int)stringToCharArray[i];
				 ascii = ascii*j;
				 
			}
			System.out.println("product of ascii values="+ascii);

	}
}