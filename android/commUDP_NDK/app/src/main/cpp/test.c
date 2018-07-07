//
// Created by Taner Metin on 06.07.18.
//

#include<stdio.h>

int main() {

    int i = 3;
    int *j = &i;
    printf("%p\n", j);
    printf("%p\n", &i);
    printf("%d\n", *j);
}

