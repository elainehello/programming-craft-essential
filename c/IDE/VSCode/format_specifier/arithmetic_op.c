#include "core.h"

void    is_numeric(int x, int y) {
    int   rs, sub;

    rs = x + y;
    sub = x - y;
    printf("%d %d\n", rs, sub);
}

void    is_float(float x, float y) {
    float   rs, sub;

    rs =  x + y;
    sub = x - y;
    printf("%.1f %.1f\n", rs, sub);
}
