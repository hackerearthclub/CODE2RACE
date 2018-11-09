#include <stdio.h>
int main(void) 
{
	int i,j,n,t,k,a[100];
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
    		scanf("%d %d",&n,&k);
    		for(j=0;j<n;j++)
    		{
       			scanf("%d",&a[j]);
    		}
    		for(j=0;j<n;j++)
    		{
        		if(a[j]<=k)
        		{
            			k=k-a[j];
           	 		printf("1");
        		}
        		else
            			printf("0");
    		}
    		printf("\n");
	}
}
