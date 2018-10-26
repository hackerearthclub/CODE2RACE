#include <stdlib.h>
#include <stdio.h>


int		ft_countword(char *str)
{
	int index;
	int total;

	index = 0;
	total = 0;
	while (str[index])
	{
		if (str[index] != '\t' && str[index] != ' ' && str[index] != '\n'
				&& (str[index + 1] == ' ' || str[index + 1] == '\t'
					|| str[index + 1] == '\0' || str[index + 1] == '\n'))
		{
			total++;
		}
		index++;
	}
	return (total);
}

char	**ft_malloctab(char *str, char **tab)
{
	int index;
	int index_tab;
	int count;

	index = 0;
	index_tab = 0;
	while (str[index])
	{
		while (str[index] == ' ' || str[index] == '\t' || str[index] == '\n')
		{
			index++;
		}
		if (str[index] != '\0')
		{
			count = 0;
			while (str[index] != ' ' && str[index] != '\t'
					&& str[index] != '\0' && str[index] != '\n')
			{
				count++;
				index++;
			}
			tab[index_tab] = (char*)malloc(count + 1);
			index_tab++;
		}
	}
	return (tab);
}

char	**ft_filltab(char *str, char **tab)
{
	int index;
	int index_tab;
	int	index_word;

	index = 0;
	index_tab = 0;
	while (str[index])
	{
		while (str[index] == ' ' || str[index] == '\t' || str[index] == '\n')
		{
			index++;
		}
		if (str[index] != '\0')
		{
			index_word = 0;
			while (str[index] != ' ' && str[index] != '\t'
					&& str[index] != '\0' && str[index] != '\n')
			{
				tab[index_tab][index_word] = str[index];
				index_word++;
				index++;
			}
			tab[index_tab][index_word] = '\0';
			index_tab++;
		}
	}
	tab[index_tab] = NULL;
	return (tab);
}

char    **ft_split(char *str)
{
	int		nb_words;
	char	**tab;

	nb_words = ft_countword(str);
	tab = (char**)malloc(sizeof(char*) * (nb_words + 1));
	tab = ft_malloctab(str, tab);
	tab = ft_filltab(str, tab);
	return (tab);
}

int	main(void)
{
	char msg[1024];
	printf("Enter a sentence : ");
	gets(msg);
	char **tab = ft_split(msg);
	int count = ft_countword(msg) - 1;
	if (count >= 0)
	{
		while (count > 0)
		{
			printf("%s ", tab[count]);
			count--;
		}
		printf("%s\n", tab[0]);
	}
	else
	{
		printf("Sentence error\n");
	}
	return 0;
}
