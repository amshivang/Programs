import java.util.*;

public class Name
{
    boolean test(String a, String b)
    {
        if(a.length()!=b.length())
            return false;
        char[] arr = a.toCharArray();
        Arrays.sort(arr);
        a = new String(arr);
        arr = b.toCharArray();
        Arrays.sort(arr);
        b = new String(arr);
        return a.equals(b);
    }
    public static void main(String args[])
    {
        Scanner in = new Scanner(System.in);
        int i = in.nextInt();
        while(i-- > 0){
            int m = in.nextInt();
        String s,t;
        s = in.next();
        t = in.next();
        Name n = new Name();
        if(n.test(s,t))
            System.out.println("YES");
        else
            System.out.println("NO");
    }
    }
}