#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int h = get_int("number of horizontal:");
    //prompt for a positive number
    while( h <= 0)
    {
        h = get_int("enter positive integer:");
    }

    for(int i = 0; i < h ; i++)
    {
        printf("#");
    }
    printf("\n");

    int v = get_int("number of vertical:");
    //prompt for a positive number
    {
    while( v <= 0)
        v = get_int("enter positive integer:");
    }

    for(int i = 0; i < v ; i++)
    {
        printf("#\n");
    }

     int m = get_int("matrix dimension:");
    //prompt for a positive number
    {
    while( m <= 0)
        m = get_int("enter positive integer:");
    }

    for(int i = 0; i < m ; i++) //rows
    {
        for(int j = 0; j < m ; j++) //coloumns
        {
            printf("#");
        }
        printf("#\n");
    }

}
