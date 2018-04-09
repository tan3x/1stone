#include <stdio.h>
#include <cs50.h>

// Prints half pyramid

int main(void)
{

    int height = get_int("Height:");

    while (height < 8 || height > 23)
    {
        height = get_int("Height:");

    }
    if (height == 0 )
    {
        return 0;
    }

    int width = height - 1;

    if (height >= 8 && height <= 23 || height ==1 || height == 2)
    {
        for (int i = 0; i < height; i++)
        {
            //print gaps
            for (int j = 0; j < width - i; j++)
            {
                printf(" ");
            }
            //print hashes

            for (int k = 0; k < i + 2; k++)
            {
                printf("#");
            }
            printf("\n");

        }




    }

}
