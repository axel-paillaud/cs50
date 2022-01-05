#include <stdio.h>
#include <stdlib.h>

typedef struct person
{
    struct person *parents;
    char c;
}
person;

int gen = 3;

person *create_family(int generation);

int main(void)
{
   person *p = create_family(gen);
   person *list = p;

   for (person *tmp = list; tmp != 0; tmp = tmp->parents)
   {
       printf("%c\n", tmp->c);
   }
}

person *create_family(int generation)
{
    person *p = malloc(sizeof(person));

    if (generation > 1)
    {
        p->c = 'A';
        p->parents = create_family(generation - 1);
    }
    else
    {
        p->parents = NULL;
        p->c = 'O';
    }

    return p;
}