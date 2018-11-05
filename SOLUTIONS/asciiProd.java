import java.util.Scanner;
public class asciiProd  { 
   
public static long productAscii(String str) { 
    long prod = 1; 
  
    for (int i = 0; i < str.length(); i++)   { 
        prod *= str.charAt(i); 
    } 
  
  
    return prod; 
} 
  
 
public static void main(String[] args) { 
   // String str = "BiD";  
       Scanner scanner = new Scanner(System.in);
       String str = scanner.nextLine();
    System.out.println(productAscii(str)); 
} 
} 