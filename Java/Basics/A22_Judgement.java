import java.util.Scanner;

public class A22_Judgement {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Give me 10$");
        int amount = in.nextInt();
        if ( amount >= 10 ) {
            // get ticket
            System.out.println("*****************");
            System.out.println("*Ticket for Java*");
            System.out.println("*   Price:10$   *");
            System.out.println("*****************");
            // change
            System.out.println("Change: " + (amount - 10));
        } else {
            if (amount > 0)
                switch (amount) {
                case 1:
                    System.out.println("Get out here!");
                    break;
                case 2:
                    System.out.println("Are you kiding me?");
                    break;
                default:
                    System.out.println("I need 10$");
                }
            else
                System.out.println("I will call the police.");
        }
    }

}