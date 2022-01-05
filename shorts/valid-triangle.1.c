#include <stdio.h>
#include <cs50.h>

//Prototype
bool valid_triangle(float array[3]);

int main(void)
{
    float lenght[3];
    for (float i = 0; i < 3; i++)
        {
            float [i] = get_float("côté: ");
        }

   float triangle = valid_triangle(lenght[3]);

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
bool valid_triangle(float array[3])
{
    //check if all of the integers are positive integers
    if (array[0] < 0 || array[1] < 0 || array[2] < 0)
    {
        return false;
    }

    //check if the sum of two side is not less than the third side
    if ((array[0] + array[1]) < array[2] || (array[1] + array[2]) < array[0] || (array[2] + array[0]) < array[1])
    {
        return false;
    }

    return true;
}