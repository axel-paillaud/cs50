#include <stdio.h>
#include <cs50.h>

int main(void)

{
    //Prompt the user for positive integer between 1 and 8
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    //Print out the height the user choose
    int d = 7;
    for (int i = 0; i < n; i++)
    {
        //Print out spaces to right align the pyramid
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