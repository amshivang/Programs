#include <stdio.h>

int main()
{
    int n;
    printf("Enter a number: ");
    if (scanf("%d", &n) != 1)
    {
        printf("Invalid input\n");
        return 1;
    }

    char one[][20] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
                      "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
    char ten[][20] = {"twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

    if (n < 0 || n >= 100000)
    {
        printf("one lakh or out of range");
    }
    else if (n == 0)
    {
        printf("zero");
    }
    else
    {
        // Print the thousand part if >= 1000
        if (n >= 1000)
        {
            int thousands = n / 1000;
            if (thousands < 20)
            {
                printf("%s thousand", one[thousands - 1]);
            }
            else
            {
                printf("%s", ten[thousands / 10 - 2]);
                if (thousands % 10 != 0)
                {
                    printf(" %s", one[thousands % 10 - 1]);
                }
                printf(" thousand");
            }
            n = n % 1000;
            if (n > 0)
            {
                printf(" ");
            }
        }

        // Print the hundred part if >= 100
        if (n >= 100)
        {
            printf("%s hundred", one[n / 100 - 1]);
            n = n % 100;
            if (n > 0)
            {
                printf(" ");
            }
        }

        // Print the remaining tens and units if > 0
        if (n > 0)
        {
            if (n < 20)
            {
                printf("%s", one[n - 1]);
            }
            else
            {
                printf("%s", ten[n / 10 - 2]);
                if (n % 10 != 0)
                {
                    printf(" %s", one[n % 10 - 1]);
                }
            }
        }
    }
    printf("\n");
    return 0;
}