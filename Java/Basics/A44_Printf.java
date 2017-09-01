import java.util.Scanner;

public class A44_Printf {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        double sum = 0.0;
        int sign = 1;
        for ( int i =1; i<=n; i++, sign = -sign) {
            sum += sign+1.0/i;
            // i ++;
            // sign = -sign;
        }
        System.out.println(sum);
        System.out.printf("%.2f",sum);
    }
}