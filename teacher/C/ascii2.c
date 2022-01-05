#include <stdio.h>

int main(void)

{
    char alphabet[24];
    alphabet[0] = 97;

    for (alphabet[0] = 97; alphabet[0] < 123; alphabet[0]++)
    {
        printf("%c", alphabet[0]);
    }
    printf("\n");
}
