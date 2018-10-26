#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char	*new_tab(char *str);
void	fill_tab(char *src, char *dest, int size);

char	*new_tab(char *str)
{
	char *tab;
	int len = strlen(str);
	tab = (char *)malloc(sizeof(char)*(len+1));
	tab[len] = '\0';
	fill_tab(str, tab, len);
	return tab;
}

void	fill_tab(char *src, char *dest, int size)
{
	int c1 = 0;
	int c2 = size-1;
	while (c2 >= 0)
	{
		dest[c1] = src[c2];
		c2--;
		c1++;
	}
}

int	main(int argc, char **argv)
{
	if (argc != 2)
	{
		printf("Argument error !\n");
		return 1;
	}
	else
	{
		char *reverse;
		reverse = new_tab(argv[1]);
		if (!strcmp(argv[1], reverse))
		{
			printf("Palindrome\n");
		}
		else
		{
			printf("Not a palindrome\n");
		}
	}
	return 0;
}
