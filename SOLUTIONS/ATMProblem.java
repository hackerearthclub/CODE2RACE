import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class ATMProblem {
    public static void main(String ... args) {

        Scanner scanner = new Scanner(System.in);
        int testNums = Integer.parseInt(scanner.nextLine());
        StringBuilder sb = new StringBuilder();
        for(;testNums > 0; testNums --){
            int units = lineToIntegers(scanner.nextLine()).get(1);
            Iterator<Integer> withdraws = lineToIntegers(scanner.nextLine()).iterator();
            while(withdraws.hasNext()){
                Integer withdraw = withdraws.next();
                if(withdraw <= units){
                    units -= withdraw;
                    sb.append(1);
                }else{
                    sb.append(0);
                }
            }
            sb.append(" ");
        }
        System.out.print(sb.toString());
    }

    private static List<Integer> lineToIntegers(String line){
        return Arrays.stream(line.split(" ")).map(val -> Integer.parseInt(val)).collect(Collectors.toList());
    }
}
