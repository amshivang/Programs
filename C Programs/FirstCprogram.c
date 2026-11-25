#include <stdio.h>

int main(void) {
    int a, b, c, d, e;
    printf("Enter marks of 5 subjects:\n");
    if (scanf("%d %d %d %d %d", &a, &b, &c, &d, &e) != 5) {
        printf("Invalid input.\n");
        return 1;
    }
    double pct = (a + b + c + d + e) * 100.0 / 500.0;
    printf("The percentage is %.2f%%\n", pct);
    return 0;
}
