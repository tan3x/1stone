// Helper functions for music
#include <stdio.h>
#include <cs50.h>
#include <math.h>
#include "helpers.h"
#include <string.h>


// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
int duration(string fraction)
{
    if(fraction[0] == '1')
    {
        if(fraction[2] == '8')
        {
            return 1;
        }
        else if(fraction[2] == '4')
        {
            return 2;
        }
        else if(fraction[2] == '2')
        {
            return 4;
        }
        else if(fraction[2] == '1')
        {
            return 8;
        }
    }
    else if(fraction[0] == '3' && fraction[2] == '8')
    {
        return 3;
    }
    else
    {
        return 0;
    }
    return 0;
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    int n = 0;
    int octave;
    if (strlen(note)==3){
        octave = atoi(&note[2]);
        //printf("%c\n",note[1]);
        char accident = note[1];
        //printf("%c\n", accident);
        if (accident=='#')
        {
            //printf("found a sharp");
            n += 1;
        }
        else if (accident == 'b')
        {
            //printf("found a flat");
            n -= 1;
        }
    }
    else
    {
        octave = atoi(&note[1]);
    }
    char letter = note[0];

    if (letter=='A'){
        n += 0;
    }else if (letter=='B'){
        n += 2;
    }else if (letter=='C'){
        n -= 9;
    }else if (letter=='D'){
        n -= 7;
    }else if (letter=='E'){
        n -= 5;
    }else if (letter=='F'){
        n -= 4;
    }else if (letter=='G'){
        n -= 2;
    }
    //printf("%i\n",n);
    n += (octave-4) * 12;

    float power = n/12.;
    //printf("%f\n",power);
    float f = round(pow(2, power)*440);
    //printf("%f\n",f);
    return f;
}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    if (strcmp(s,"")==0)
    {
        return 1;
    }

    else

    {
        return 0;
    }

}
