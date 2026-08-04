#include <stdio.h>
#include <math.h>

int main()
{
    printf("ax² + bx + c = 0\n enter a, b and c: ");
    int a,b,c;
    scanf("%d %d %d", &a, &b, &c);
    int d = b*b - 4*a*c;
    float r1,r2;
    r1 = ((-b)+sqrt(d)) / (2*a);
    r2 = ((-b)-sqrt(d)) / (2*a);
    printf("Roots are: %f and %f", r1, r2);
}