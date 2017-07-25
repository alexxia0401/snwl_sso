#include <stdio.h>

int main()
{
    void print_star();
    void print_message();
    print_star();
    print_message();
    print_star();
    return 0;
}

void print_star() {
    int i;
    for (i = 0; i < 16; i++)
        printf("*");
    printf("\n");    
}

void print_message() {
    printf("How do you do!\n");
}
