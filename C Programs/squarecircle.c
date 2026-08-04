#include <stdio.h>

int main() {
    float side, radius;
    printf("Enter the side length of the square: \n");
    scanf("%f", &side);
    printf("Enter the radius of the circle: \n");
    scanf("%f", &radius);
    if (side > (2 * radius))
    {
        printf("The square can fit inside the circle.\n");
    }
    else
    {
        printf("The square cannot fit inside the circle.\n");
    }
    printf("The area of the square is: %f\n", side * side);
    printf("The area of the circle is: %f\n", 3.14 * radius * radius);
    return 0;
}
