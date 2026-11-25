import java.util.Scanner;

public class root {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter coefficients a, b, and c: ");
            double a = sc.nextDouble();
            double b = sc.nextDouble();
            double c = sc.nextDouble();

            if (a == 0) {
                if (b == 0) {
                    System.out.println(c == 0 ? "Infinite solutions." : "No solution.");
                } else {
                    System.out.println("Linear root: " + (-c / b));
                }
                return;
            }

            double discriminant = b * b - 4 * a * c;
            if (discriminant > 0) {
                double root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
                double root2 = (-b - Math.sqrt(discriminant)) / (2 * a);
                System.out.println("Two distinct real roots: " + root1 + " and " + root2);
            } else if (discriminant == 0) {
                double r = -b / (2 * a);
                System.out.println("One repeated real root: " + r);
            } else {
                double realPart = -b / (2 * a);
                double imagPart = Math.sqrt(-discriminant) / (2 * a);
                System.out.println("Complex roots: " + realPart + " + " + imagPart + "i and " + realPart + " - " + imagPart + "i");
            }
        }
    }
}
