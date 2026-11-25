#include <stdio.h>

int main(void) {
    int n;
    printf("Enter a number: ");
    if (scanf("%d", &n) != 1) {
        printf("Invalid input.\n");
        return 1;
    }

    int sign = n < 0 ? -1 : 1;
    long long abs_n = n < 0 ? -(long long)n : (long long)n;

    if (abs_n < 10) {
        printf("%d\n", n);
        return 0;
    }

    long long p = 1;
    long long temp = abs_n;
    while (temp >= 10) {
        temp /= 10;
        p *= 10;
    }

    long long first = abs_n / p;
    long long last = abs_n % 10;
    long long middle = (abs_n % p) / 10;
    long long swapped = (last * p + middle * 10 + first) * sign;

    printf("%lld\n", swapped);
    return 0;
}
