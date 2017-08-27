import java.util.Scanner;

public class A32_DoWhile {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int number = in.nextInt();
        int count = 0;
        do {
            number /= 10;
            count ++;
        } while ( number > 0 );
        System.out.println(count);
    }
}