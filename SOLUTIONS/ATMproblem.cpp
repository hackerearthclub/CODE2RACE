#include <stdio.h>

int ans[200];

int main ()
{
	int t, n, a;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		int p = 0;
		scanf("%d%d", &n, &a);
		for (int j = 0; j < n; j++)
		{
			int x;
			scanf("%d", &x);
			if (a - x >= 0)
			{
				ans[p++] = 1;
				a -= x;
			}
			else
			{
				ans[p++] = 0;
			}
		}
		for (int j = 0; j < p; j++)
		{
			printf("%d", ans[j]);
			ans[j] = 0;
		}
		printf("\n");
	}
	return 0;
}