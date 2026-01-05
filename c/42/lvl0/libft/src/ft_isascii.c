#include "../inc/libft.h"

int ft_isascii(int c)
{
    if (c >= 0 && c <= 127)
        return (1);
    else
        return (0);
}
/* int main()
{
    printf("%d %d\n", ft_isascii(0), ft_isascii(128));
    return(0);
} */
