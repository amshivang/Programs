#include <stdio.h>

int main() {
    int a,b,c,d,e,f;
    float g;
    printf("Enter subject of 5 number: \n");
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    scanf("%d", &d);
    scanf("%d", &e);
    scanf("%d", &f);
    g = (a + b + c+ d + e + f) * 100.0 / 500;
    printf("The percentage is %f \n", g);
    return 0;
}