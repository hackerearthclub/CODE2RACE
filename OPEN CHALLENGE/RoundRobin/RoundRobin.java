import java.io.*;
import java.io.FileInputStream;
import java.util.*;

@SuppressWarnings({"unchecked","deprecation","cast"})
public class RoundRobin {
  
    public static void main(String[] args) throws IOException {
        
        //Output files created
        PrintStream o1 = new PrintStream(new FileOutputStream("OutputFile1.txt",true));
        PrintStream o2 = new PrintStream(new FileOutputStream("OutputFile2.txt",true));
        PrintStream o3 = new PrintStream(new FileOutputStream("OutputFile3.txt",true));
        
        String choice="";
        int l=0;
        
        do
        {
            System.out.println("--------------------------------------------------------------");
            System.out.println("Enter Input File name:");
            System.out.println("--------------------------------------------------------------");
            String filename = "";
        
            Scanner sc = new Scanner(System.in);
            filename = sc.nextLine();  //Filename from whih contents are to be copied
            BufferedReader br = new BufferedReader(new FileReader(filename));
            // Declaration of objects to read data
            String line = br.readLine();

            System.out.println("");
            System.out.println("--------------------------------------------------------------");
            System.out.println("File Elements: " + line);
            System.out.println("--------------------------------------------------------------");
            System.out.println("");

            // Data is split into Array
            String strArr[] = line.split(" ");

            // Data is alloted to files according to RoundRobin form
            for(int i=0;i<strArr.length;i++) {

                if(l%3==0) {
                    o1.print(strArr[i]+" ");
                }
                if(l%3==1) {
                    o2.print(strArr[i]+" ");
                }
                if(l%3==2) {
                    o3.print(strArr[i]+" ");
                }
                l++;
            }
            System.out.println("Do you want to add elements from another file : YES/NO");
            // Choice is taken from user whether he wants to add more elements or not 
            choice = sc.nextLine();

        }while(choice.equals("YES"));

        o1.flush();
        o2.flush();
        o3.flush();

        o1.close();
        o2.close();
        o3.close();
       
    }
}