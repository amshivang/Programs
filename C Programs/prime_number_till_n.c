#include <stdio.h>

int main() {
    printf("Enter the range till where perfect numbers are to be printed: ");
    int n;
    scanf("%d", &n);
    for(int i=2; i<n; i++) {
        int c = 0;
        for(int j=2; j<=i/2; j++) {
            if(i%j==0) {
                c = 1;
                break;
            }
        }
        if(c==0) {
            if(i==2) {
                printf("%d", i);
            } else {
                printf(", %d", i);
            }
        }
    }
    return 0;
}