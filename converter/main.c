#include <stdio.h>
#include "converter.h"
int main() {
    printf("How many inches?\n");
    float i;
    if (scanf("%f", &i) == 0){
        printf("Invalid input. Please input valid floating point numbers.\n");
        return 1;
    }
    float cm = convert(i);
    printf("%.2f inches is %.2f cm\n", i, cm);
    return 0;

}
