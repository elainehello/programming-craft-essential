#ifndef LIBFT_H
#define LIBFT_H

#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>

char    *ft_substr(char const *s, unsigned int start, size_t len);
size_t  ft_strlen(const char *s);
int     ft_atoi(const char *nptr);
char    *ft_strchr(const char *s, int c);
int     ft_isascii(int c);
int     ft_isalpha(int c);

#endif