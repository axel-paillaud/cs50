#include <stdio.h>
#include <cs50.h>

//prototype
int fibonacci(int x, int y, int z);

int a = 0;
int b = 1;
int c;

int main (void)
{
    printf("%i\n%i\n", a, b);
    fibonacci(a, b, c);
}

int fibonacci(int x, int y, int z)
{

    if ( z < 233)
    {
        z = x + y;
        printf ("%i\n", z);
        x = y;
        y = z;
        return fibonacci(x, y, z);
    }
    else
    {
        return 0;
    }
}