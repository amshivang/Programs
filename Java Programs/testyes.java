import java.util.*;

public class yesoryes
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		String s = in.next();
		int i = s.indexOf("Y");
		System.out.println(i);
		System.out.println(s.indexOf("Y",i+1));
		}
}