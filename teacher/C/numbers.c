#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int numbers[] = {8, 5, 1, 6, 1, 1, 6, 2, 3, 8, 5, 4, 9, 9, 5, 6};
    int biggest_numbers = 0;

    for (int i = 0; i < 16; i++)
    {
        if (numbers[i - 1] > biggest_numbers)
        {
            biggest_numbers = numbers[i - 1];
        }
    }

    for (int j = 0; j < 16; j++)
    {
        if (biggest_numbers == numbers[j])
        {
            printf("%i\n", numbers[j]);
        }
    }
}