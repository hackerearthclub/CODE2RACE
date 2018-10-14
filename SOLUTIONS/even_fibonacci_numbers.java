import java.util.Scanner;

public class even_fibonacci_numbers {

    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int cases = Integer.parseInt(s.nextLine());
        for(;cases > 0; --cases){
            int max = Integer.parseInt(s.nextLine());
            if(max < 2){
                System.out.println("0");
            } else {
                int fib1 = 1;
                int fib2 = 2;
                int sum = 2;
                while(true){
                    int temp = fib2;
                    fib2 = 2 * fib1 + 3 * fib2;
                    fib1 = fib1 + 2 * temp;
                    if(fib2 >= max){
                        break;
                    }
                    sum += fib2;
                }
                System.out.println(sum);
            }
        }
    }
}
