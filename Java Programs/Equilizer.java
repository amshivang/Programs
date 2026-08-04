import java.util.*;

public class Equilizer {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        while (t-- > 0) {
            int n = in.nextInt(); 
            int k = in.nextInt(); 
            int[] a = new int[n];
            int sum = 0;
            for (int i = 0; i < n; i++) {
                a[i] = in.nextInt();
                sum += a[i];
            }
            if (sum % 2 == 1 || (n * k) % 2 == 1) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}
