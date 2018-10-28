#include <stdio.h>
void main() 
{
	int i,j,n,t,a[100];
  long k,a[100]s;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
    		scanf("%d %ld",&n,&k);
    		for(j=0;j<n;j++)
    		{
       			scanf("%ld",&a[j]);
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
