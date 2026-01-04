#include "../inc/libft.h"

/* char *ft_substr(char const *s, unsigned int start, size_t len)
{
    int     str_len;
    char    *sub_str;
    int     i;
    int     i_pos;

    str_len = ft_strlen(s);
    if ((str_len < start) && ((str_len - start) > len)) {
        sub_str = malloc(sizeof(str_len - start));
        if (!sub_str)
            return (NULL);
        i = 0;
        i_pos = str_len - start;
        while(i >= i_pos)
            sub_str[i++] = s[i_pos++];
        sub_str[i] = '\0';
        return sub_str;
    }
} */

char *ft_substr(char const *s, unsigned int start, size_t len)
{
    size_t s_len;
    char    *sub_str;
    size_t  i;

    if (!s)
        return(NULL);
    s_len = ft_strlen(s);
    if (start >= s_len) {
        sub_str = malloc(sizeof(char*));
        if (!sub_str)
            NULL;
        sub_str[0] = '\0';
        return sub_str;
    }
    if (s_len - start < len)
        len = s_len - start;
    sub_str = malloc(len + 1);
    if (!sub_str)
        return (NULL);
    i = 0;
    while (i < len) {
        sub_str[i] = s[start + i];
        i++;
    }
    sub_str[i] = '\0';
    return (sub_str);
}

int main(void) {
    const char *str = "Hello, World";
    unsigned int start = 5;
    size_t len = 4;
    char *res;

    res = ft_substr(str, start, len);
    printf("original str: %s\n", str);
    printf("result: %s\n", res);

    return (0);
}