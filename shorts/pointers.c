#include <stdio.h>
#include <cs50.h>

int main(void)
{
    char c;
    c = 'A';
    char* pc;
    pc = &c;

    printf("%c\n", *pc);
    printf("%p\n", pc);
}