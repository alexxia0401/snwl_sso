#include <stdio.h>

int main()
{
    void hanoi(int, char, char, char);
    int m;
    printf("Input the number of diskes: ");
    scanf("%d", &m);
    printf("The step to move %d diskes:\n", m);
    hanoi(m, 'A', 'B', 'C');
}

void hanoi(int n, char one, char two, char three) {
    void move(char, char);
    if (n == 1) {
        move(one, three);
    } else {
        hanoi(n - 1, one, three, two);
        move(one, three);
        hanoi(n - 1, two, one, three);
    }
}

void move(char x, char y) {
    printf("%c-->%c\n",x, y);
}
