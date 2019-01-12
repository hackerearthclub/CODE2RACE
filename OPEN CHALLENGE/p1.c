#include<stdio.h>
#include<conio.h>
void main()
{
    int i,j,k,a;
    scanf("%d",&a);
    for(i=1;i<=a;i++)
    {
            for(j=1;j<=i;j++)
            {
                    printf("*");
            }
            for(k=(2*a)-2;k>=i;k--)
            {
                if(k<=(2*i)-1)
                    printf("*");
                else printf(" ");

            }

            printf("\n");

    }

    getch();
}
