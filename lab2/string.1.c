#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    int score = 0;
    string s = get_string("Input: ");
    printf("Output: ");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        score = score + s[i];
    }
    printf("%i\n", score);
}