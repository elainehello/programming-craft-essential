#include "../inc/libft.h"

int ft_isalpha(int c)
{
    if (c >= 65 && c <= 90)
        return (1);
    else if (c >= 97 && c <= 122)
        return (1);
    else
        return (0);
}

/* int main()
{
    int l = 'a';
    printf("%d %d\n", ft_isalpha(l), ft_isalpha(1));
    return (0);
} */
