import java.util.Scanner;

public class A12_Calculate {

    public static void main(String[] args) {
        System.out.println("Hello");
        // Length Unit Converter
        int foot;
        double inch;
        final double coefficient = 0.3048;
        Scanner in = new Scanner(System.in);
        // print and no wrap
        System.out.print("Input foot and inch:");
        foot = in.nextInt();
        inch = in.nextDouble();
        System.out.println("foot=" + foot + ",inch=" + inch);
        double meter = (foot + inch / 12.0) * coefficient;
        System.out.println((int)(meter * 100) + "cm");
    }

}