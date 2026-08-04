import java.util.*;

public class square
{
	public static void main(String args[])
	{
	Scanner in = new Scanner(System.in);
	int n;
	n = in.nextInt();
	while(n-- > 0){
	int a,b,c,d;
	a = in.nextInt();
	b = in.nextInt();
	c = in.nextInt();
	d = in.nextInt();
	if(a == b && b == c && c == d)
	System.out.println("YES");
	else 
	System.out.println("NO");
	}
	}
}