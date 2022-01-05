#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{

    int letters = 0;

    if (argc > 2 || argc < 2)
    {
        printf ("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        string s = argv[1];
        int k = atoi(s);

        for (int i = 0, n = strlen(s); i < n; i++)
        {
            int c = s[i];
            if (isalpha(c))
            {
                letters = 1;
            }
        }

        if (letters == 1)
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
        else
        {
            printf("Votre key est %i\n", k);

            string plaintext = get_string("plaintext: ");
            printf("ciphertext: ");

            for (int i = 0, n = strlen(plaintext); i < n; i++)
            {
                char c = plaintext[i];
                printf("%c", c + k);
            }
            printf("\n");

        }
    }
}