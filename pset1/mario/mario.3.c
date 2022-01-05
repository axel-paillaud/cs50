#include <stdio.h>
#include <cs50.h>

int main(void)

{
    //Demander un nombre entre 1 et 8 à l'utilisateur
    int n;
    do
    {
       n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j == 8 - n; j++)

        {
            printf("#");
        }
    printf("\n");
    }
}