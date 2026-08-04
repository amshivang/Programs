#include <stdio.h>
int sum(int a, int b) {
    return a + b;
}
int product(int a, int b) {
    return a * b;
}
int division(int a, int b) {
    return a / b;
}
int subtract(int a, int b) {
    return a - b;
}
int main() {
    int c;
    printf("Enter your choice:\n1. Sum\n2. Product\n3. Division\n4. Subtraction\n");
    scanf("%d", &c);
    switch(c) {
        case 1: {
            int a, b;
            printf("Enter two numbers to be added:\n ");
            scanf("%d %d", &a, &b);
            printf("Sum: %d\n", sum(a, b));
            break;
        }
        case 2: {
            int a, b;
            printf("Enter two numbers to be multiplied:\n");
            scanf("%d%d",&a,&b);
            printf("Product: %d\n", product(a, b));
            break;
        }
        case 3: {
            int a, b;
            printf("Enter two numbers to be divided:\n");
            scanf("%d %d", &a, &b);
                printf("Division: %d\n", division(a, b));
            break;
        }
        case 4: {
            int a, b;
            printf("Enter two numbers to be subtracted:\n ");
            scanf("%d %d", &a, &b);
            printf("Subtraction: %d\n", subtract(a, b));
            break;
        }
        default:
            printf("Invalid choice!\n");
        return 0;
    }
}