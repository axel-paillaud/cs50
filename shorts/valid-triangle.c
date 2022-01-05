#include <stdio.h>
#include <cs50.h>

//Prototype
bool valid_triangle(float a, float b, float c);

int main(void)
{
   float x = get_float("premier chiffre: ");
   float y = get_float("deuxième chiffre: ");
   float z = get_float("troisième chiffre: ");

   int triangle = valid_triangle(x, y, z);

   if (triangle == false)
   {
        printf("C'est faux ! On ne peux pas faire un triangle avec ces 3 chiffres.\n");
   }
   else
   {
       printf("Correct ! On peut faire un triangle avec ces 3 chiffres. \n");
   }
}

//function of checking if we can do a triangle with this number or not.
bool valid_triangle(float a, float b, float c)
{
    //check if all of the integers are positive integers
    if (a < 0 || b < 0 || c < 0)
    {
        return false;
    }

    //check if the sum of two side is not less than the third side
    if ((a + b) < c || (b + c) < a || (c + a) < b)
    {
        return false;
    }

    return true;
}