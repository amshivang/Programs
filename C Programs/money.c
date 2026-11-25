#include <stdio.h>

int main(void) {
    int n;
    printf("Enter the amount in Rs: ");
    if (scanf("%d", &n) != 1 || n < 0) {
        printf("Invalid amount.\n");
        return 1;
    }

    const int denominations[] = {2000, 500, 200, 100, 50, 20, 10, 5, 2, 1};
    const int count = (int)(sizeof(denominations) / sizeof(denominations[0]));

    for (int i = 0; i < count; i++) {
        int denom = denominations[i];
        if (n >= denom) {
            int notes = n / denom;
            printf("The count of %d Rs notes is %d => %d\n", denom, notes, notes * denom);
            n %= denom;
        }
    }
    return 0;
}
