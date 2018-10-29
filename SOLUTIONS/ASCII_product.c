#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int	main(void)
{
	char str[64];
	printf("Enter characters : ");
	gets(str);
	int len = strlen(str)-1;
	int count = 0;
	int total = 1;
	while (count <= len)
	{
		total *= str[count];
		count++;
	}
	printf("Result : %d\n", total);
	return 0;
}
