#include <stdio.h>

int main()
{
    int max(int x, int y);
    int a, b, c;
    printf("Pls. input two numbers(e.g. 3,4): ");
    scanf("%d,%d", &a, &b);
    c = max(a, b);
    printf("max == %d\n", c);
    return 0;
}

int max(int x, int y)
{
    int z;
    if(x > y)
        z = x;
    else
        z = y;
    return z;
}
