#include<stdio.h>

int main()
{
int t,p, count[10]={0},a[20],i,j,k;

scanf("%d",&t);

    for(i=0;i<t;i++)
    {
        scanf("%d", &p);
        for(j=0;j<p;j++)
        {
            scanf("%d", &a[j]);
            if(a[j] % 2 == 0)
            {
                count[i] = count[i] + 1;

            }

        }

    }
    for(k=0;k<t;k++)
    {
        printf("%d\n", count[k]);
    }

    return 1;
}
