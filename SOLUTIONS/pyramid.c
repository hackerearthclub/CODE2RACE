#include <stdio.h>
int main()
{
    int rows, i, j,k, number= 1;

    printf("Enter number of rows: ");
    scanf("%d",&rows);

    for(i=1; i <= rows; i++)
    {
    	for(k=rows;k>i;k--)
    	{
    		printf(" ");
        } 
        for(j=1; j <= 2*i-1; ++j)
        {
        	printf("*");
	    } 

        printf("\n");
    }
    return 0;
}