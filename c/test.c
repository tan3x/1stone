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


int arr[5]={13,23,33,43,53}, *p;
int a=3, d=-3,i,j,k,z[2],n,n1,n2;
static int counter=5; // compiler keeps local variable in existence during the program life
int     external;
extern void f_external();
char y[2];
struct Books {
    char title[20];
    char author[20];
    char subject[20];
    int book_id;   
};



double c=3.12345;
struct person{
    char name[50];
    int age; };
int arraysize;
//int *array = malloc(arraysize*sizeof(int));
//int  array = realloc(array, newarraysize*sizeof(int)); 

union Data { //difference between struct
   int ii;
   float ff;
   char strr; };


int main(){
    struct Books book1;
    struct Books book2;
    int *z1=&z[0],*z2=&z[1]; //same pointer?
    char *y1=&y[0],*y2=&y[1];
   // int *aptr=&a; why getting error on compile
   union Data data;
   external = 55;
    
    f_external();
    
    strcpy(book1.title, "The Doors");
    strcpy(book1.author, "of Perception");
    strcpy(book1.subject, "Subject");
    book1.book_id = 12345;
        printf( ":%s::%s:\n", book1.title,book1.author);
    





        printf("z ptr is %d %d\n",*z1,*z2);
        printf("y ptr is %d %d\n",*y1,*y2);

    while(++d<1){
        printf("\td is %d",d);
    i=1;    }
    while(counter--){
        printf(ANSI_COLOR_BLUE "\nCounter is %d.  \t" ANSI_COLOR_RESET,counter );

    i=1;    }



for (d=0; d<3; ++d){
        printf("d is %d\t",d);
    i=2;           }

switch (i){
    case 1:
        printf(ANSI_COLOR_GREEN "\nCase 1 is active\n" ANSI_COLOR_RESET );
        break;
    case 2:
        printf(ANSI_COLOR_GREEN "\nCase 2 is active\n" ANSI_COLOR_RESET);
        break;
    default:
        printf("Case is different\n");
        break;
            }

void jump(){
    for(j=0; j<10; ++j){
        printf("J is = %d\t",j);

        if(j==2){
            j=4;
            goto left;
            printf("to be skipped\n");
            continue; // continue on ++?
                } 
        else if(j==5){
            goto right;
            break;   }
        left:  printf("Left\n");  }
        right: printf("Right\n");
                return;
            }
            jump();

    int s3, s_1 = 3, s_2 = 5;
void swap(int *s1, int *s2){
   
    s3 = *s1;
    *s1 = *s2;
    *s2 = s3;
    return;  }
     
     swap(&s_1, &s_2);
        printf("Swapped values are %d, %d\n", s_1, s_2 );
        printf("Permanent addresses are %p, %p\n", &s_1, &s_2 );
    
      if (external>0) {
        for (n=0; n<5; ++n){
            printf("The %d. triangular number is:%d\n",n,(n*(n+1))/2);
                            };
        }
        else {
        printf("Enter a value bigger than 0.\n");
            }
p = arr ; 
        printf("Array values are:[%d,%d,%d,%d,%d]\n",*(p+0),*(p+1),*(p+2),*(p+3),*(p+4));

        }
    



