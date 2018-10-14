import java.util.ArrayList;
import java.util.Scanner;

public class Sum_Factorial_digit {
    public static void main(String[] args) {

        int cases,number;
        long factorial,temp,sum;

        Scanner scanner = new Scanner(System.in);
        ArrayList<Long> ans = new ArrayList<>();

        cases = scanner.nextInt();

        for (int i = 0; cases>i; i++){

            sum = 0;
            factorial =1;

            number=scanner.nextInt();

            for(temp=1;temp<=number;temp++){
                    factorial *= temp;
            }

            for (temp =factorial; temp>0; temp/=10){
                sum  += temp%10;
            }
            ans.add(sum);
        }

        for (cases= 0; cases<=ans.size()-1; cases++)
            System.out.println(ans.get(cases));
    }
}
