#include <stdio.h>

int main()
{
    char c;
    printf("Enter any character");
    scanf("%c", &c);

    if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
    {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            printf("vowel");
        else
            printf("consonant");
    }

    if (c >= '0' && c <= '9')
        printf("Digit");
    else
        printf("Special character");

    return 0;
}
