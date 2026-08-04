#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
    srand(time(NULL));
    int number = rand()%100 +1;
    printf("Guess the number I'm thinking of (between 1 and 100): ");
    printf("\nEnter the number you guessed: ");
    int guess;
    scanf("%d", &guess);
    while(guess != number)
    {
        if(number<guess)
        {
            printf("Enter a smaller number: ");
            scanf("%d", &guess);
        }
        else
        {
        printf("Enter a larger number: ");
        scanf("%d", &guess);
        }
    }
    printf("You guessed it correctly !");
    return 0;
}