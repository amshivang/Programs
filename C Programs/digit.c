#include <stdio.h>  
#include <math.h>

int main()  
{  
    int n,a,b,o=0,m=0,x,d=0,c,p; 
    printf("Enter a number: ");  
    scanf("%d", &n);
    c=n;
    for(int i=0; n>0; i++)
    {
        n /= 10;
        d++;
    }
    p = round(pow(10,d-1));
    a = c/p;
    b = c%10;
    x = c%p;
    m = x / 10;
    o= b*p + m*10 +a;  
    printf("%d\n", o);
    return 0;  
}