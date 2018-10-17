import java.util.Scanner;

public class str2int {

	public static void main(String[] args) {
	   Scanner s1 = new Scanner(System.in);
	   String input = s1.next();
	   int ans = convertStringToInt(input);
	   System.out.println(ans);
	}
	public static int convertStringToInt(String input){
		if(input.length()==1)
          return input.charAt(0) - '0';
      int a =convertStringToInt(input.substring(1));
       int b = input.charAt(0) - '0';
        double ans = b*(Math.pow(10,input.length()-1)) + a;
        return (int) ans;
	}

}
