#include <stdio.h>

int sum(int n)
{
    int s=0;
    for(int i=0; n > 0; i++)
    {
    s+=n%10;
    n/=10;
    }
    return s;
}

int rsum(int n)
{
    if(n<10)
    return n;
    return n%10 + rsum(n/10);
}

int main()
{
    int n;
    printf("Enter a 5 digit number : ");
    scanf("%d", &n); 
    printf("Sum of the digits is : %d \n", sum(n));
    printf("Sum of the digits calculated by recursion is : %d ", rsum(n));
    return 0;
}