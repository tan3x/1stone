#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define CONSTANT = 3.14;
#define ANSI_COLOR_RED     "\x1b[31m"
#define ANSI_COLOR_GREEN   "\x1b[32m"
#define ANSI_COLOR_YELLOW  "\x1b[33m"
#define ANSI_COLOR_BLUE    "\x1b[34m"
#define ANSI_COLOR_RESET   "\x1b[0m"

typedef int boolean;
#define true 1
#define false 0

typedef struct node{
    int number2;
    struct node *next;
}
node;


int capacity;

int * getrandomfunc(){
    static int stvar[10];
    int i;
    srand((unsigned) time(NULL));

    for ( i = 0; i < 3; ++i) {
        stvar[i] = rand();
        printf("stvar[%d]=%d\n", i , stvar[i] );
     }
        return stvar;
    }

int main(){

    int var1=11, var2[5], *var3, **var4;
    int a, b, c;
    a = 10;
    b = 20;
   printf(" sddsdf %d\n",a++);
   printf(" sddsdf %d\n",a++);
   printf(" sddsdf %d\n",a++);


    var3 = &var1;
    var4 = &var3;
    
    
    printf("Add: %p, %p, %p, %d, %d\n", &var1, &var2, var3, *var3, **var4);
    int  *ptr, i; 

    ptr = getrandomfunc();
	
    for ( i = 0; i < 3; i++ ) {
        printf("*(ptr + [%d]) : %d is at %p \n", i, *(ptr + i), (ptr + i)  );
     }
    char str[1000];
     FILE *fp ;
     fp = fopen("./sil.txt", "w+");
     fprintf(fp, "test message\n");
     //fputs("fput testing",fp);
     fgets(str,10000,fp);
     puts(str); // doesnt print string
     fclose(fp);

     int x = 10, y = 100%90, ik;
     for(ik=1; ik<10; ik++)
     if(x != y)
         printf("x = %d y = %d\n", x, y);

     
do{
        //capacity = get_int("capacity: ");
        printf("capacity: ");
        scanf("%i", &capacity);
    }
    while(capacity<1);

    //memory for numbers
    int numbers[capacity];
    boolean found = false;
    int number;


    int size = 0;
    while (size < capacity){

        //int number = get_int("number: ");
        printf("number: ");
        scanf("%i", &number);

        for ( int i = 0; i<size; i++){
            if (numbers[i] == number){
                found = true ; 
                break;
            }

        }

        if(!found){
            numbers[size]= number;
            size++;
        }
    }

    for (int i; i < size; i++){
        printf("%i\n", numbers[i]);
    }
    return 0;
}



