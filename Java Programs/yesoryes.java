import java.util.*;

public class Yesoryes
{
	
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		Yesoryes o = new Yesoryes();
		int n;
		n = in.nextInt();
		while(n-- > 0){
		String s = in.next();
		if(s.contains("YY"))
			System.out.println("NO");
		else 
			System.out.println("YES");
		}
	}
}