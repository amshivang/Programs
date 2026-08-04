#include <stdio.h>
int main() {
    int n,l=0;
    int consent = 1;
    printf("Enter a number: ");
    scanf("%d",&n);
    do{
        printf("Enter another number: ");
        scanf("%d",&l);
        if(n>l)
        l=n;
        printf("The largest Number so far is %d\n",l);
        printf("Do you want to continue? (1 for Yes / 0 for No): ");
        scanf("%d",&consent);
    }
    while(consent == 1);
    printf("The largest Number is %d\n",l);
    return 0;
}   