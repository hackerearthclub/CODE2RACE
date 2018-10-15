
import java.util.*;

public class Rock_Paper_Scissor {
    public static void main(String args[]) {
        display();
    }

    public static void display() {
        Scanner in = new Scanner(System.in);
        System.out.println("Welcome to rock ,paper and scissors game");

        System.out.println("Enter your option : rock,paper or scissior");
        String choice = in.next();
        comp_select(choice);

    }

    public static void comp_select(String choice) {
        String[] comp = {"rock", "paper", "scissors"};
        Random rnd = new Random();
        int index = rnd.nextInt(comp.length);
        String computer = comp[index];
        System.out.println("Your choice : " + choice);
        System.out.println("Computer's choice : " + computer);
        validate(choice, computer);

    }

    public static void validate(String choice, String computer) {


        int win = 0;
        int lose = 0;
        if (choice.equals(computer)) {
            System.out.println("Its a tie,play again...");
            display();
        } else if (choice.equals("rock") && computer.equals("paper"))
            //System.out.println("You lose,Computer wins...Enter (Y/N) to play game again or not");
            lose = 1;

        else if (choice.equals("rock") && computer.equals("scissors"))
            //System.out.println("You win !!! Enter (Y/N) to play game again or not");
            win = 1;

        else if (choice.equals("paper") && computer.equals("scissors"))
            //System.out.println("You lose,Computer wins...Enter (Y/N) to play game again or not");
            lose = 1;

        else if (choice.equals("paper") && computer.equals("rock"))
            //System.out.println("You win !!! Enter (Y/N) to play game again or not");
            win = 1;

        else if (choice.equals("scissors") && computer.equals("paper"))
            //System.out.println("You win !!! Enter (Y/N) to play game again or not");
            win = 1;

        else if (choice.equals("scissors") && computer.equals("rock"))
            //System.out.println("You lose,Computer wins...Enter (Y/N) to play game again or not");
            lose = 1;
        result(win, lose);
    }

    public static void result(int win, int lose) {
        Scanner in = new Scanner(System.in);
        if (win == 1) {
            System.out.println("You win !!!");
        } else if (lose == 1) {
            System.out.println("You lose,Computer wins...");
        }
        System.out.println("Wanna play again ?(Y/N)");
        String xyz = in.next();
        if (xyz.equalsIgnoreCase("y"))
            display();
        else
            System.out.print("Good bye... !!");
    }

}

