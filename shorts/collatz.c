#include <stdio.h>
#include <cs50.h>

//prototype
int collatz (int n);
int steps = 0;

int main(void)
{
    int n = get_int("Numbers: ");
    collatz(n);

}

int collatz(int n)
{

    if (n == 1)
    {
        printf("collatz :%i\n", steps);
        return 0;
    }
    else if ((n % 2) == 0)
    {
        steps++;
        return 1 + collatz(n/2);
    }
    else
    {
        steps++;
        return 1 + collatz(3*n + 1);
    }
}