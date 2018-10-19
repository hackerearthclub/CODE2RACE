#include<stdio.h>

int calcFilledBottles(int sum);

void main()
{
    int testCase, no_of_bottles, bottles[1000], i, j, ans[1000];
    
    scanf("%d",&testCase);
    
    for(j = 0; j < testCase; j++)
    {
        int sum = 0;
        scanf("%d",&no_of_bottles);
        for(i = 0; i < no_of_bottles; i++)
        {
            scanf("%d",&bottles[i]);
        }
        
        for(i = 0; i < no_of_bottles; i++)
        {
            sum = sum + bottles[i];
        }
        ans[j] = calcFilledBottles(sum);
    }
    for(i = 0; i < testCase; i++)
    {
        printf("%d",ans[i]);
        printf("\n");
    }
}

int calcFilledBottles(int sum)
{
    int filled_bottles = 0;
    
    filled_bottles = sum / 100;
    
    return filled_bottles;

}
    
    
