package hacktober;

import java.util.Scanner;

public class compress {

	public static void main(String[] args) {
		Scanner s1 = new Scanner(System.in);
		String input = s1.next();
		String output = compress(input);
		System.out.println(output);
	}
	public static String compress(String inputString) {
		int x = inputString.length();
        int i=0;
       String result="";
      int count=1;
       while(i<x-1){  
         char ch1=inputString.charAt(i);
         char ch2=inputString.charAt(i+1);
         if(ch1==ch2){
           count=count+1;
         }
         else{
            if(count!=1)
              result=result+ch1+count;
            else
              result=result+ch1;
            count=1;
         }
           
         i++;
       }
     
      char ch3=inputString.charAt(x-1);
        if(count!=1)
             result=result+ch3+count;
        else
             result=result+ch3;
     return result;
	}


}
