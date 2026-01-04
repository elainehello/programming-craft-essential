#include "../inc/libft.h"

size_t ft_strlen(const char *s)
{
    size_t i;

    i = 0;
    while (s[i])
        i++;
    return (i);
}

/* int main(void)
{
    const char *s;

    s = "Hello";
    printf("%zu\n", ft_strlen(s));
    return (0);
} */
