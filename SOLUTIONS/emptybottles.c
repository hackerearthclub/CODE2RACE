#include <stdio.h>

int main(void)
{
        int t,n,a[1000],i,j,tv,tn;
        scanf("%d",&t);
        for(i=0;i<t;i++)
        {
            tv=0;
            scanf("%d",&n);
            for(j=0;j<n;j++)
            {
                scanf("%d",&a[i]);
                tv=tv+a[i];
            }
            tn=tv/100;
            if(tv%100>=50)
                tn++;
            printf("%d\n",tn);
        }
        return 0;
}
