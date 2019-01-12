#include <stdio.h>

void main()
{
    char str[80];
    printf("Enter the string  : ");
    scanf("%s",str);
    int i;
    for(i=0;str[i]!=NULL;i++);
    int flag=0,len=i;
    for(i=0;i<len;i++)
    {
        if(str[i]!=str[len-i-1])
        {
            flag=1;
            break;
        }
    }
    if(flag==0)
        printf("Indeed");
    else
        printf("Not at all");
}
