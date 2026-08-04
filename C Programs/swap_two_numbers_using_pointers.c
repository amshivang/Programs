#include <stdio.h>
int main()
{
    int a,b;
    printf("Enter two numbers to be swapped using pointers:\n");
    scanf("%d",&a);
    scanf("%d",&b);
    int *p1 = &a;
    int *p2 = &b;
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
    printf("After swapping: a = %d, b = %d\n", *p1, *p2);
    return 0;
}