#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Get numbers from user
    int x = get_int("x: ");
    int y = get_int("y: ");

    // Divide x by y
    float z = (float) x / (float) y;

    //Affiche le résultat sur l'écran
    printf("%f\n", z);
}