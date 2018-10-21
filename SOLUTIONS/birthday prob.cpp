#include<iostream>
using namespace std;
int main()
{
int t,n;
char c[100000];
cin>>t;

for(int i=0;i<t;i++)
    {
        cin>>n;

        for(int i=0;i<n;i++)
        {
           cin>>c[i];
           cout<<c[i]<<" ";
        }


         int sum=0;
        for(int i=0;i<n;i++)
        {
            sum=c[i]+sum;
        }
        if(sum%n==0)
        {
            int med, flag=0;
            med=sum/n;
            for (int i=0;i<n;i++)
            {
                if(med<c[i])
                {
                    flag=flag+c[i]-med;
                }
                else
                {continue;}
            }
            cout<<flag;
        }
        else
        {
        cout<<"No Treat";
        }

    }


return 0;
}
