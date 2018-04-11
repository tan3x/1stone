#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

/*
USAGE: given text will be crypted by number provided as argument
$ ./caesar 1
plaintext:  HELLO
ciphertext: IFMMP
*/

int main(int argc, string argv[])
{
    //reject inputs other than 2
    if (argc < 2 || argc > 2)
    {
        printf("Usage ./caesar k\n");
        return 1;
    }
    //translate string to integer
    int k = atoi(argv[1]);

    //get text input from user
    string text = get_string("Enter the message:");
    int n = strlen(text);

    //printinf title before loop
    printf("ciphertext:");

    //iterate over text
    for (int i = 0; i < n; i++)
    {
        //validity of text
        if (isalpha(text[i]))
        {
            if isupper(text[i])
            {
                printf("%c", (((text[i]) + k - 65) % 26) + 65);
            }
            else if islower(text[i])

                printf("%c", (((text[i]) + k - 97) % 26) + 97);
        }

        //adds un-alphanumerical character at the end of string.
        else
            printf("%c", text[i]);

    }
    printf("\n");
    return 0;
}
