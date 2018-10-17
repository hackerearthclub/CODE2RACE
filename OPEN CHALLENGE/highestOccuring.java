
import java.util.Scanner;

public class highestoccuring {

	public static void main(String[] args) {
		Scanner s1 = new Scanner(System.in);
		   String input = s1.next();
		   char ans = highestOccuringCharacter(input);
		   System.out.println(ans);

	}
	public static char highestOccuringCharacter(String inputString) {
		int arr[]= new int[256];
      int max=-1,index=0;
      char ch,ch1;
      for(int i=0;i<inputString.length();i++){
        arr[inputString.charAt(i)]++;
      }
       ch1=inputString.charAt(0);
      index=arr[ch1];
      for(int j=0;j<inputString.length();j++){
        ch=inputString.charAt(j);
        if(arr[ch]>index){
          index=arr[ch];
          ch1=ch;
        }
      }
      return ch1;
	}

}
