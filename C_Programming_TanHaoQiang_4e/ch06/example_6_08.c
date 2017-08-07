#include <stdio.h>
#include <string.h>

int main()
{
    const int STR_LEN = 81;
    char string[STR_LEN];
    int i, num = 0, word = 0;
    char c;
    /* gets() is dangerous and should not be used. */
    /* gets(string); */
    fgets(string, STR_LEN, stdin);
    string[strlen(string) - 1] = '\0';
    for (i = 0; (c = string[i]) != '\0'; ++i) {
        if (c == ' ') {
            word = 0;
        } else if (word == 0) {
            word = 1;
            num++;
        }
    }
    printf("There are %d words in this line.\n", num);
    return 0;
}
