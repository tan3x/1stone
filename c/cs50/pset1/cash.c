#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    int dime = 0;
    float total;
    int cent = 0;

    total = get_float("Quanto cuesta:");

    while (total <= 0)
    {
        total = get_float("Quanto cuesta:");
    }
    cent = roundf(total*100) ;

    while (cent >= 25)
    {
        cent = cent - 25;
        dime += 1;
    }

    while (cent >= 10)
    {
        cent = cent - 10;
        dime += 1;
    }
    while (cent >= 5)
    {
        cent = cent - 5;
        dime += 1;
    }

    while (cent >= 1)
    {
        cent = cent - 1;
        dime += 1;
    }

    printf("%d\n", dime);
}
