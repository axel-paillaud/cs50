#include <stdio.h>
#include <cs50.h>

int main(void)
{
    char *s = "Hi!!";
    printf("%s\n", s);
    printf("%c\n", *(s+1));
    printf("%c\n", *(s+2));
    printf("%c\n", *(s+3));
}