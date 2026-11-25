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
		int best = a;
		if (l > 0) {
			int step = Math.floorMod(b, l);
			int cur = Math.floorMod(a + step, l);
			while (cur != a) {
				if (cur > best) {
					best = cur;
				}
				cur = Math.floorMod(cur + step, l);
			}
		}
		System.out.println(best);
	}
	}
}