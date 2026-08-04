#include <stdio.h>

int main()
{
    float radius, area, volume;

    printf("Enter the radius of the circle: \n");
    scanf("%f", &radius);   
    area = 3.14 * radius * radius;
    printf("The area of the circle is: %f\n", area);

    printf("Enter the radius of the sphere: \n");
    scanf("%f", &radius);
    area = 4 * 3.14 * radius * radius;
    volume = (4.0f / 3.0f) * 3.14 * radius * radius * radius;
    printf("The surface area of the sphere is: %f\n", area);
    printf("The volume of the sphere is: %f\n", volume);

    return 0;

}