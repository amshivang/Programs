#include <stdio.h>

int main(void) {
    char c;
    printf("Enter any character: ");
    if (scanf(" %c", &c) != 1) {
        return 1;
    }

    if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
        char lower = (c >= 'A' && c <= 'Z') ? (char)(c - 'A' + 'a') : c;
        if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u') {
            printf("Vowel\n");
        } else {
            printf("Consonant\n");
        }
    } else if (c >= '0' && c <= '9') {
        printf("Digit\n");
    } else {
        printf("Special character\n");
    }

    return 0;
}
