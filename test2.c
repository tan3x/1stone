#include <stdio.h>
#define CONSTANT = 3.14;
#define ANSI_COLOR_RED     "\x1b[31m"
#define ANSI_COLOR_GREEN   "\x1b[32m"
#define ANSI_COLOR_YELLOW  "\x1b[33m"
#define ANSI_COLOR_BLUE    "\x1b[34m"
#define ANSI_COLOR_RESET   "\x1b[0m"

extern int external;
int internal;

void f_external(){
    if (external || internal){
        internal = external--;
         printf(ANSI_COLOR_BLUE "External value is %d\n" ANSI_COLOR_RESET, external);
         printf(ANSI_COLOR_BLUE"Internal value is %d\n"  ANSI_COLOR_RESET, internal);
    }
}

