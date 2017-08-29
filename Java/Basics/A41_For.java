import java.util.Scanner;

public class A41_For {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int factor = 1;
        // int i = 1;
        // while (i<=n) {
        //     factor = factor*i;
        //     i = i+1;
        // }
        for (int i=1;i<=n;i++) {
            factor *= i;
        }
        System.out.println(factor);
    }
}