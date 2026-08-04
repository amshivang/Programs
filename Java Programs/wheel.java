import java.util.*;

public class wheel
{
	public static void main(String agrs[])
	{
		Scanner in = new Scanner(System.in);
		int t;
		t = in.nextInt();
		while(t-- > 0)
		{
		int l, a, b;
		l = in.nextInt();
		a = in.nextInt();
		b = in.nextInt();
		int c = a;
		while ((a + b) % l != a)
			a = (a+b)%l;
		System.out.println(a);
	}
	}
}