import java.util.Scanner;

public class A42_Break {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int amount = in.nextInt();
        bill:
        for ( int one = 0; one <= amount; ++one) {
            for (int five = 0; five <= amount/5; ++five) {
                for (int ten = 0; ten <= amount/10; ++ten) {
                    for (int twenty = 0; twenty <= amount/20; ++twenty) {
                        if (one+five*5+ten*10+twenty*20 == amount) {
                            System.out.println(one + " 1$\n" + five + " 5$\n" + ten + " 10$\n" + twenty + " 20$");
                            break bill;  // continue
                        }
                    }
                }
            }
        }
    }
}