#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //prototype
    int collatz(n);
    
    
    int collatz(int n)
    {
        int steps = 1;
        do
        {
            if (n == 1)
            {
                printf("collatz :%i\n", steps);
                return 0;
            }
            else if ( n % 2 == 0)
            {
                n /= 2;
                steps++;
            }
            else
            {
                n = 3 * n + 1;
                steps++;
            }
        }
        while (n > 1)
    }
}