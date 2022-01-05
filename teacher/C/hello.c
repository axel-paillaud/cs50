#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string("Comment tu t'appelles ?");
    printf("hello, %s", answer);
}