#include <stdio.h>

static long long int_pow(int base, int exp) {
    long long result = 1;
    for (int i = 0; i < exp; i++) {
        result *= base;
    }
    return result;
}

int main(void) {
    int n;
    printf("Enter an upper bound: ");
    if (scanf("%d", &n) != 1 || n < 0) {
        printf("Invalid input.\n");
        return 1;
    }

    int printed = 0;
    for (int j = 0; j <= n; j++) {
        int digits = (j == 0) ? 1 : 0;
        for (int t = j; t > 0; t /= 10) {
            digits++;
        }

        long long sum = 0;
        for (int t = j; t > 0; t /= 10) {
            sum += int_pow(t % 10, digits);
        }

        if (sum == j) {
            printf("%s%d", printed ? ", " : "", j);
            printed = 1;
        }
    }
    printf("\n");
    return 0;
}
