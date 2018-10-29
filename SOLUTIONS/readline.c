#include <stdio.h>
#define MAX 100
int main()
{
	char buf[MAX];
	fgets(buf, MAX, stdin);
	printf("string is: %s\n", buf);

	return 0;
}
