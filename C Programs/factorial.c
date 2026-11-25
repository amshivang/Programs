#include <stdio.h>

int main(void) {
    int n;
    printf("Enter a non-negative integer: ");
    if (scanf("%d", &n) != 1 || n < 0) {
        printf("Invalid input. Please enter a non-negative integer.\n");
        return 1;
    }

    unsigned long long fact = 1;
    for (int i = 2; i <= n; i++) {
        fact *= (unsigned long long)i;
    }

    printf("Factorial of %d = %llu\n", n, fact);
    return 0;
}
