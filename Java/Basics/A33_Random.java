import java.util.Scanner;

public class A33_Random {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int number = (int)(Math.random()*100+1);    //  [0,1) -->[0,100) -->(int)[1,100) == [1,100]
        int a;
        int count = 0;
        do {
            a = in.nextInt();
            count = count + 1;
            if (a > number) {
                System.out.println("Biger");
            }
            else if (a < number) {
                System.out.println("Smaller");
            }
        } while (a != number);
        System.out.println("Congratulation,You guessed "+ count +" times.");
    }
}