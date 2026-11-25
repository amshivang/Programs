#include <stdio.h>

int main(void) {
    int largest, num;
    int consent = 1;

    printf("Enter a number: ");
    if (scanf("%d", &largest) != 1) {
        printf("Invalid input.\n");
        return 1;
    }

    do {
        printf("Enter another number: ");
        if (scanf("%d", &num) != 1) {
            break;
        }
        if (num > largest) {
            largest = num;
        }
        printf("The largest Number so far is %d\n", largest);
        printf("Do you want to continue? (1 for Yes / 0 for No): ");
        if (scanf("%d", &consent) != 1) {
            break;
        }
    } while (consent == 1);

    printf("The largest Number is %d\n", largest);
    return 0;
}
