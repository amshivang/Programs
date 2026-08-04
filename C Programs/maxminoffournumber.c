#include <stdio.h>

int main()
{
    int num1, num2, num3, num4;
    printf("Enter four numbers: \n");
    scanf("%d", &num1);
    scanf("%d", &num2);
    scanf("%d", &num3);
    scanf("%d", &num4);
    int max = num1;
    int min = num1;
    if (num2 > max) max = num2;
    if (num3 > max) max = num3;
    if (num4 > max) max = num4;
    if (num2 < min) min = num2;
    if (num3 < min) min = num3;
    if (num4 < min) min = num4;
    printf("Maximum: %d\n", max);
    printf("Minimum: %d\n", min);
    return 0;
}