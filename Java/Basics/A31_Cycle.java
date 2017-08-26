import java.util.Scanner;

public class A31_Cycle {

    public static void main(String[] args) {
        // Double in Java
        Scanner in = new Scanner(System.in);
        int number = in.nextInt();
        int count = 0;
        while ( number > 0 ) {
            number /= 10;
            count ++;
        }
        System.out.println(count);
    }
}