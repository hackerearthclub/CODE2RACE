#include<stdio.h>
#include<conio.h>
void main(){
int x,i,count=0;
printf("enter 5 nos");
for(i=0;i<6;i++)
{
    scanf("%d", &x);
    if(x>count)
        count=x;
}
printf("greatest no is %d",x );
getch();
}
