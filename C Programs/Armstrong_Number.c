#include <stdio.h>

int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    int m;
    int x=0;
    for(int j=0; j<=n; j++)
    {
        m=j;
        int sum = 0;
        for(int i=0; m>0; i++){
        int digit = m%10;
        sum += digit*digit*digit;
        m /= 10;
        }
        if(sum==j&&x==0)
        {
            printf("%d", j);
            x=1;
        }
        else if(sum==j)
        printf(", %d", j);
    }
    return 0;
}
