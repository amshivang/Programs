#include <stdio.h>
void fab(int a, int b, int n)
{
    int c = a + b;
    for (int i=0; i<n; i++) {
    printf("%d ", a);
    c = a +b; 
    a = b;
    b = c;
    }
}
int main() {
    int n, i = 0, j = 1;
    printf("Enter the number: ");
    scanf("%d", &n);
    printf("Fibonacci Series: ");
    fab(i,j,n);
    return 0;
}