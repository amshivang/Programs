#include <stdio.h>

int main() {
    printf("Enter the amount in Rs: ");
    int n;
    scanf("%d", &n);
    if(n>=2000)
    printf("The count of 2000 Rs notes is %d => %d\n",n/2000, n/2000*2000);

    n=n%2000;

    if(n>=500)
    printf("The count of 500 Rs notes is %d => %d\n",n/500, n/500*500);

    n=n%500;

    if(n>=200)
    printf("The count of 200 Rs notes is %d => %d\n",n/200, n/200*200);

    n=n%200;

    if(n>100)
    printf("The count of 100 Rs notes is %d => %d\n",n/100, n/100*100);

    n=n%100;

    if(n>50)
    printf("The count of 50 Rs notes is %d => %d\n",n/50, n/50*50);

    n=n%50; 

    if(n>20)
    printf("The count of 20 Rs notes is %d => %d\n",n/20, n/20*20);

    n=n%20;

    if(n>10)
    printf("The count of 10 Rs notes is %d => %d\n",n/10, n/10*10);

    n=n%10;

    if(n>5)
    printf("The count of 5 Rs notes is %d => %d\n",n/5, n/5*5);

    n=n%5;

    if(n>2)
    printf("The count of 2 Rs notes is %d => %d\n",n/2, n/2*2);

    n=n%2;
    if(n>0)
    printf("The count of 1 Rs notes is %d => %d\n",n, n);
}