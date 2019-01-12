package check_keyword;

import java.util.Scanner;

/**
 * By Ayomie
 */
public class matrices{
    public static void main(String[] args){
        
        //let us make the program collect inputs
        int[][] mat = new int[2][2];
        Scanner input = new Scanner(System.in);
        for (int row = 0; row < 2; row++){
            System.out.print("Row" + row + ":");
            for (int col = 0; col < 2; col++){
               mat[row][col] = input.nextInt(); 
                
            }
    //System.out.println();
}
        //displayiny inputs
        for (int row = 0; row < 2; row++){
            for (int col = 0; col < 2; col++){
                System.out.print(mat[row][col] + "\t");
            }
             System.out.println();
    }
}
}