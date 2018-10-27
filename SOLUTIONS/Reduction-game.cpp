#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t,i,n,j,k;
    long s;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        scanf("%d%d",&n,&k);
        int a[n];
        for(j=0;j<n;j++)
            scanf("%d",&a[j]);
        sort(a,a+n);
        if(a[n-2]<=k)
        {
            s=accumulate(a,a+n,0);
            printf("%ld\n",s);
        }
        else
        {
           auto pos=upper_bound(a,a+n,k);
           for(auto m=pos;m!=(a+n-1);m++)
           {
               *m=k;
	             *(m+1)=*(m+1)-((*m)-k));
           }
           
           s=accumulate(a,a+n,0);
           printf("%ld\n",s);
        }
    }
   
    return 0;
}
