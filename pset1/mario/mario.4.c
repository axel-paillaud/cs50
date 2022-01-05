#include <stdio.h>
#include <cs50.h>

int main(void)

{

    int n;
    do
    {
       n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    int d = 7;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < d; j++)
        {
            printf(" ");
        }
        for (int j = -1; j < i; j++)

        {
            printf("#");
        }
        printf("\n");
        d = d - 1;
    }
}