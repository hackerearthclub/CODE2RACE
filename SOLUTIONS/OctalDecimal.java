/*
*
*   Developed by Imran Shad  for hactoberfest open source projects
*
*
*   Number System conversion from decimal to octal
*   Or from Octal to decimal
*/
import java.util.Stack;

import static java.lang.Math.pow;

public class OctalDecimal {

    /*
    Convert octal integer to decimal
    *@param {int}
    */

    public static int octalToDecimal(int x){
        int i = 0, res = 0;
        while(x > 0){
            res += (x % 10) * pow(8,i);
            x /= 10;
            i++;
        }
        return res;
    }

    /*
    Convert Decimal integer to Octal
    *@param {int}
    */

    public static int decimalToOctal(int x){
        Stack<Integer> s=new Stack();
        int res = 0;
        do{
            s.push(x % 8);
            x /= 8;
        }while(x / 8 > 0);
        s.push(x % 8);
        //rebuild
        while(!s.empty()){
            res = res * 10 + s.firstElement();
            s.pop();
        }
        return res;

    }
    public static void main(String[] args) {
        System.out.println("Hello World!");
        System.out.println(OctalDecimal.octalToDecimal(20));
        System.out.println(OctalDecimal.decimalToOctal(20));
    }
}

