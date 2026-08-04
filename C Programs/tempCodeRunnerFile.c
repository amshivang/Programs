#include <stdio.h>
 
int main()
{
    int n;
    printf("Enter a number : ");
    scanf("%d", &n);
    while(n>2)
    {
        printf("%d", (n%10)%2);
        n/=10;
    }
}