// java program to print reverse  
// of words in a string. 
import java.io.*; 
import java.util.*; 
import java.lang.*; 
  
class ReverseWordOrder 
{ 
static String wordReverse(String str) 
{ 
    int i = str.length() - 1; 
    int start, end = i + 1; 
    String result = ""; 
      
    while(i >= 0) 
    { 
        if(str.charAt(i) == ' ') 
        { 
            start = i + 1; 
            while(start != end) 
                result += str.charAt(start++); 
              
            result += ' '; 
              
            end = i; 
        } 
        i--; 
    } 
      
    start = 0; 
    while(start != end) 
        result += str.charAt(start++); 
      
    return result; 
} 
  
// Driver code 
public static void main(String[] args) 
{ 
    String str = "My name is Michele"; 
      
    System.out.print(wordReverse(str)); 
} 
} 
