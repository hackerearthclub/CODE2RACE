import java.util.*;
import java.io.*;
public class Mystery
{
    public static void main (String[] args) throws java.lang.Exception {

        final long startTime = System.currentTimeMillis();
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {

            int n = sc.nextInt();
            int even = n / 2;
            int odd = n - even;

             long extra = (long)((odd * (odd - 1)) * even) / 2;
            long extra1 = (long)(even * (even - 1) * (even - 2)) / 6;
            System.out.println(extra + extra1);}
            final long endTime = System.currentTimeMillis();
            System.out.println("Total execution time: " + (endTime - startTime));
        }


    }
