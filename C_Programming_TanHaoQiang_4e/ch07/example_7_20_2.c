#include <stdio.h>
#include <string.h>

void enter_string(char str[80]) {
    /* gets() is dangerous and should not be used. */
    /* gets(str); */
    printf("Pls. input string: ");
    fgets(str, 80, stdin);
    str[strlen(str) - 1] = '\0';
}
