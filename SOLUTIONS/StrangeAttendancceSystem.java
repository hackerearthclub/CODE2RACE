/* IMPORTANT: Multiple classes and nested static classes are supported 

https://www.hackerearth.com/problem/algorithm/strange-attendance-system-192a459f/

*/

/*
 * uncomment this if you want to read input.
//imports for BufferedReader
import java.io.BufferedReader;
import java.io.InputStreamReader;

//import for Scanner and other utility classes
*/
import java.util.*;


// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

class TestClass {
    public static void main(String args[] ) throws Exception {
        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();
        while(t>0){
            int x=sc.nextInt(),y=sc.nextInt();
            float val=((((float)y)/x)*100);
            //#System.out.println(x+"-->"+y+"-->"+val);
            if(val>=75){
                System.out.println(0);
            }else{
                System.out.println(3*x-4*y);
            }
            
            t--;
        }

        // Write your code here

    }
}
