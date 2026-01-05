#include "../inc/libft.h"

int  ft_atoi(const char *nptr)
{
    int i;
    int sign;
    int nbr;

    i = 0;
    nbr = 0;
    sign = 1;
    while (nptr[i] == ' ' || (nptr[i] >= '\t' && nptr[i] <= '\r'))
        i++;
    if (nptr[i] == '+' || nptr[i] == '-')
        if (nptr[i++] == '-')
            sign = -1;
    while (nptr[i] >= '0' && nptr[i] <= '9')
        nbr = nbr * 10 + nptr[i++] - '0';
    return (sign * nbr);
}

/* int main() {
    const char *str = "\t\r\n 42";
    int res = ft_atoi(str);

    printf("%d\n", res);
    return(0);
} */