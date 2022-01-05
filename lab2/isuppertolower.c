#include <stdio.h>
#include <ctype.h>
#include <cs50.h>
#include <string.h>

int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};


int main(void)
{
    string word = "ENCULE";
    int score = 0;

    for (int i = 0, n = strlen(word); i < n; i++)
    {
        int c = word[i];

        if (isupper(c))
        {
            c = (tolower(c));
        }

        c = c - 97;
        score = score + POINTS[c];

    }
    printf("%i\n", score);

}