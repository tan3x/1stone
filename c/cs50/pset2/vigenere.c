/*
USAGE: given text will be crypted by number provided as argument
$ ./vigenere ee
plaintext:  bb
keyword: ee
ciphertext: ff
*/

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>



int main(int argc, string argv[])
{
    //reject inputs other than 2
    if (argc < 2 || argc > 2)
    {
        printf("Usage ./vigenere keyword\n");
        return 1;
    }


    //get text input from user
    string text = get_string("Enter the plaintext:");

    int n = strlen(text);
    int n2 = strlen(argv[1]);

    //does not accept un-alphanumerical chars
    for ( int i=0; i < n2; i++)
    {
        if ( isalpha(argv[1][i]) == false )
        {
            printf("enter key with alphanumerical chars.\n");
            return 1;
        }
    }

    //print header before loop
    printf("ciphertext:");

    //iterate over text
    for (int i = 0, j = 0; i < n; i++)
    {

        char key = (argv[1][ j % n2]);
        //validity of text

        if (isupper(key)){
            key -= 65;
        }
        else if (islower(key)){
            key -= 97;
        }

        if isupper(text[i])
        {
            printf("%c", (((text[i]) + key - 65) % 26) + 65);
            j++;
        }
        else if islower(text[i])
        {
            printf("%c", (((text[i]) + key - 97) % 26) + 97);
            j++;
        }

        //adds un-alphanumerical character at the end of string.
        else{
            printf("%c", text[i]);
        }

    }
    printf("\n");
    return 0;
}

