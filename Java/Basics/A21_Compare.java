import java.util.Scanner;
import java.lang.Math;

public class A21_Compare {

    public static void main(String[] args) {
        // Double in Java
        double a = 0.1, b = 1.2 - 1.1;
        System.out.println("1.2-1.1=" + b);
        System.out.println("a=0.1,b=1.2-1.1");
        System.out.println("a==b: " + (a == b)); //fales
        System.out.println("a==b: " + (Math.abs(a - b) < 1e-6)); //true
    }

}