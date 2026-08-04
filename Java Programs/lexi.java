import java.util.*;

public class lexi {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        while (t-- > 0) {
            int n = in.nextInt(); 
            String[] arr = new String[n];
            for (int i = 0; i < n; i++) {
                arr[i] = in.next();
            }
            String s = arr[0];
            for (int i = 1; i < n; i++) {
                String option1 = s + arr[i]; 
                String option2 = arr[i] + s; 
                if (option1.compareTo(option2) <= 0) {
                    s = option1;
                } else {
                    s = option2;
                }
            }

            System.out.println(s);
        }
    }
}