/*#include <stdio.h>

int main()
{
    int i,n, t1 = 0, t2 = 1, nextTerm = 0, last;

    //i==pint"printf("Enter the number of terms: ");
    scanf("%d", &n);

    //printf("Fibonacci Series: ");

    for (i = 1; i <= n+2; ++i)
    {
        // Prints the first two terms.
        if(i == 1)
        {
            //printf("%d, ", t1);
            continue;
        }
        if(i == 2)
        {
            //printf("%d, ", t2);
            continue;
        }
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
        //printf("%d ", nextTerm);
    }
    last= nextTerm%10;
    printf("%d", last);

    return 0;

}
*/
#include<stdio.h>
 int main()
 {
 int i, n, a=0, b=1, nt=0, last, t, j=0;

scanf("%d", &t);
while(j<t)
{

 scanf("%d", &n);

 for(i=0;i<=n;i++)
 {
     if(i == 1||i==2)
     continue;

     nt= a+b;
     a=b;
     b=nt;
 }
 last=nt%10;
 printf("%d\n", last);
 j++;
}
  return 0;
 }
