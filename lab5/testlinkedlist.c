#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

typedef struct person
{
    struct person *parents[2];
    char allele[2];
}
person;

int main(void)
{
    person *branch1 = NULL;
    person *branch2 = NULL;
    person *branch3 = NULL;
    person *branch4 = NULL;
    person *p = malloc(sizeof(person));
    if (p == NULL)
    {
        return 1;
    }

    p->allele[0] = 'A';
    p->allele[1] = 'B';
    p->parents[0] = NULL;
    p->parents[1] = NULL;
    branch1 = p;
    branch2 = p;
    branch3 = p;
    branch4 = p;

    p = malloc(sizeof(person));
    if (p == NULL)
    {
        return 1;
    }
    p->allele[0] = 'B';
    p->allele[1] = 'O';
    p->parents[0] = NULL;
    p->parents[1] = NULL;
    branch1->parents[0] = p;
    branch2->parents[1] = p;

    p = malloc(sizeof(person));
    if (p == NULL)
    return 1;

    p->allele[0] = 'O';
    p->allele[1] = 'B';
    p->parents[0] = NULL;
    p->parents[1] = NULL;
    branch1->parents[0]->parents[0] = p;

    p = malloc(sizeof(person));
    if (p == NULL)
    return 1;

    p->allele[0] = 'A';
    p->allele[1] = 'B';
    p->parents[0] = NULL;
    p->parents[1] = NULL;
    branch2->parents[0]->parents[1] = p;

    for (person *tmp = branch1; tmp != NULL; tmp = tmp->parents[0])
    {
        printf("%c, %c\n", tmp->allele[0], tmp->allele[1]);
    }
}