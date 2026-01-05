#include "../inc/libft.h"

char    *ft_strchr(const char *s, int c)
{
    unsigned char uc = (unsigned char)c;

    while (*s)
    {
        if ((unsigned char)*s == uc)
            return ((char *)s);
        *s++;
    }
    if (uc == '\0')
        return ((char *)s);
    return (NULL);
}

/* int main() {
    const char *s = "test0nbr one";
    int c = 48;

    printf("original: %s -> output: [%s]", s, ft_strchr(s, c));
    return (0);
} */
