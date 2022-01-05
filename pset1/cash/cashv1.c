#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    //Prompt the user for a positive float numbers
    float change;
    int coins;
    do
    {
        change = get_float("Change owed: ");
    }
    while (change < 0);

    //round the cents to the nearest penny
    int cents = round(change * 100);

    for (coins = 0; cents >= 25; coins++)
    {
        cents = cents - 25;
    }

    for (coins = coins + 0; cents >= 10; coins++)
    {
        cents = cents - 10;
    }

    for (coins = coins + 0; cents >= 5; coins ++)
    {
        cents = cents - 5;
    }

    for (coins = coins + 0; cents >= 1; coins++)
    {
        cents = cents - 1;
    }

    printf("%i\n", coins);

}