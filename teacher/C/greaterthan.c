#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int x = get_int ("x: ");
    int y = get_int ("y: ");

    if (x < y)
    {
        printf ("x est inférieur à y\n");
    }
    else if (x > y)
    {
        printf ("x est supérieur à y\n");
    }
    else if (x == y)
    {
        printf ("x est égal à y\n");
    }
}