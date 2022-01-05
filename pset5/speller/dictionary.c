// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 1001;

unsigned int count = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    char wordcase[LENGTH + 1];
    strcpy(wordcase, word);
    for (int i = 0, n = strlen(wordcase); i < n; i++)
    {
        char c = wordcase[i];
        if (isupper(c))
        {
            c = tolower(c);
            wordcase[i] = c;
        }
    }

    unsigned int hashval = hash(wordcase);

    for (node *cursor = table[hashval]->next; cursor != NULL; cursor = cursor->next)
    {
        if (strcmp(wordcase, cursor->word) == 0)
        return true;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO
    unsigned int hashval;

    for (hashval = 0; *word != '\0'; word++)
    {
        hashval = *word + 31 * hashval;
    }
    return hashval % N;

    //hash function from the famous book : C programming language, by Brian W. Kernighan and Dennis M. Ritchie.
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *ptr = fopen(dictionary, "r");
    if (ptr == NULL)
    {
        return false;
    }

    char word[LENGTH + 1];

    for (int i = 0; i < N; i++)
    {
        table[i] = malloc(sizeof(node));
        table[i]->next = NULL;
    }

    while ((fscanf(ptr, "%s", word)) != EOF)
    {
        node *p = malloc(sizeof(node));
        if (p == NULL)
        {
            free(p);
            return false;
        }

        p->next = NULL;
        strcpy(p->word, word);
        count++;

        unsigned int hashval = hash(p->word);

        if (table[hashval]->next == NULL)
        table[hashval]->next = p;

        else
        {
            p->next = table[hashval]->next;
            table[hashval]->next = p;
        }

    }
    fclose(ptr);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return count;
}


// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        node *tmp = cursor;
        while (cursor != NULL)
        {
            cursor = cursor->next;
            free(tmp);
            tmp = cursor;
        }
    }
    return true;
}
