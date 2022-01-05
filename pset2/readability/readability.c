#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

//Prototype
int count_letters(string sentences);
int count_words(string sentences);
int count_sentences(string sentences);

int main(void)
{
    //get string from the users
    string s = get_string("Text: ");

    //compute number of letters, words and sentences
    int letters = count_letters(s);
    int words = count_words(s);
    int sentences = count_sentences(s);

    // Get an average per 100 words
    float L = letters * 100 / words;
    float S = sentences * 100 / words;

    //calculate with the Coleman-Liau formula, then round it to the nearest integer
    float indexfloat = 0.0588 * L - 0.296 * S - 15.8;
    int index = round(indexfloat);

    //print out the result
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}


//Functions
int count_letters(string sentences)
{
    int count_letters = 0;

    for (int i = 0, n = strlen(sentences); i < n; i++)
    {
        char c = sentences[i];
        if (isalpha(c))
        {
            count_letters++;
        }
        else
        {
            count_letters = count_letters + 0;
        }
    }
    return count_letters;
}

int count_words(string sentences)
{
    int count_words = 1;

    for (int i = 0, n = strlen(sentences); i < n; i++)
    {
        char c = sentences[i];

        if (isspace(c))
        {
            count_words++;
        }

        else
        {
            count_words = count_words + 0;
        }
    }
    return count_words;
}


int count_sentences(string sentences)
{
    int count_sentences = 0;

    for (int i = 0, n = strlen(sentences); i < n; i++)
    {
        char c = sentences [i];

        if (c == '.' || c == '?' || c == '!')
        {
            count_sentences++;
        }
    }
    return count_sentences;
}