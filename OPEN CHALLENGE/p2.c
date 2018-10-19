#include<stdio.h>
#include<conio.h>
void main()
{
    int i,j,k,a,m;
    scanf("%d",&a);
    for(i=1;i<=a;i++)
    {
        for(m=i; m<=a; m++)
            printf(" ");
        j=i-1;
        for(k=1;k<=i+j;k++)
            printf("*",k);
        printf("\n");
    }

    getch();
}
