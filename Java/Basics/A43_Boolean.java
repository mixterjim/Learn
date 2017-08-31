import java.util.Scanner;

public class A43_Boolean {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        boolean yes = true;
        boolean no = false;
        System.out.println(!yes);           //false
        System.out.println(!(5>4));         //false
        System.out.println(yes && no);      //false
        System.out.println(yes || no);      //true
        System.out.println(!no && (5>4));   //true
        // 1   ()
        // 2   ! + - ++ --
        // 3   * / %
        // 4   + -
        // 5   < <= > >=
        // 6   == !=
        // 7   &&
        // 8   ||
        // 9   = += -= *= /= %=
    }
}