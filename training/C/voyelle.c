#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main (void)
{
    char *input = malloc(50);

    printf("Texte: ");
    scanf("%s", input);

    int voyelle[6] = {0, 0, 0, 0, 0, 0};

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (input[i] == 'A' || input[i] == 'a')
        voyelle[0]++;

        else if (input[i] == 'E' || input[i] == 'e')
        voyelle[1]++;

        else if (input[i] == 'I' || input[i] == 'i')
        voyelle[2]++;

        else if (input[i] == 'O' || input[i] == 'o')
        voyelle[3]++;

        else if (input[i] == 'U' || input[i] == 'u')
        voyelle[4]++;

        else if (input[i] == 'Y' || input[i] == 'y')
        voyelle[5]++;
    }

    printf("A:  %i\nE:  %i\nI:  %i\nO:  %i\nU:  %i\nY:  %i\n", voyelle[0], voyelle[1], voyelle[2], voyelle[3], voyelle[4], voyelle[5]);

    free(input);
}