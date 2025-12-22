#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include "core.h"

int main(void) {
    int nbr1, nbr2;
    float fnbr1, fnbr2;

    printf("Enter integer value:\n");
    scanf("%d %d", &nbr1, &nbr2);    
    is_numeric(nbr1, nbr2);
    
    printf("Enter float value:\n");
    scanf("%f %f", &fnbr1, &fnbr2);
    is_float(fnbr1, fnbr2);
    return (0);
}

/* int main()
{
	int nbr1, nbr2;
    float fnbr1, fnbr2;
    int rs1;
    float rs2;
    
    scanf("%d", &nbr1);
    scanf("%d", &nbr2);
    rs1 = nbr1 + nbr2;
    printf("%d ", rs1);
    printf("%d\n", nbr1 - nbr2);
    
    scanf("%f", &fnbr1);
    scanf("%f", &fnbr2);
    rs2 = fnbr1 + fnbr2;
    printf("%.1f ", rs2);
    printf("%.1f", fnbr1 - fnbr2);
    
    return 0;
} */