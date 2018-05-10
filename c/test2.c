#include <stdio.h>
#include <stdlib.h>
#define CONSTANT = 3.14;
#define ANSI_COLOR_RED     "\x1b[31m"
#define ANSI_COLOR_GREEN   "\x1b[32m"
#define ANSI_COLOR_YELLOW  "\x1b[33m"
#define ANSI_COLOR_BLUE    "\x1b[34m"
#define ANSI_COLOR_RESET   "\x1b[0m"




extern int external;
int internal;
int capacity;

void f_external(){
    if (external || internal){
        internal = external--;
         printf(ANSI_COLOR_BLUE "External value is %d\n" ANSI_COLOR_RESET, external);
         printf(ANSI_COLOR_BLUE"Internal value is %d\n"  ANSI_COLOR_RESET, internal);
    }
}

int main (void){
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
}
