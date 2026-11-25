#include <math.h>
#include <stdio.h>

int main(void) {
    printf("ax^2 + bx + c = 0\nEnter a, b and c: ");
    double a, b, c;
    if (scanf("%lf %lf %lf", &a, &b, &c) != 3) {
        printf("Invalid input.\n");
        return 1;
    }

    if (a == 0.0) {
        if (b == 0.0) {
            printf("No valid equation.\n");
        } else {
            printf("Linear root: %.4f\n", -c / b);
        }
        return 0;
    }

    double d = b * b - 4.0 * a * c;
    if (d > 0.0) {
        double r1 = (-b + sqrt(d)) / (2.0 * a);
        double r2 = (-b - sqrt(d)) / (2.0 * a);
        printf("Roots are: %.4f and %.4f\n", r1, r2);
    } else if (d == 0.0) {
        printf("Repeated root: %.4f\n", -b / (2.0 * a));
    } else {
        double real = -b / (2.0 * a);
        double imag = sqrt(-d) / (2.0 * a);
        printf("Complex roots: %.4f + %.4fi and %.4f - %.4fi\n", real, imag, real, imag);
    }
    return 0;
}
