#include<bits/stdc++.h>
using namespace std;
struct answer
{
    long long int gcd,lcm;
};
long long int gcd(long long int a, long long int b) 
{ 
    if (b == 0) 
    {
        return a; 
    }
    return gcd(b, a % b); 
}
struct answer* findlcm(vector<long long int> v,long long int n) 
{ 
    struct answer * k=(struct answer *)malloc(sizeof(struct answer));
    long long int g=0,ans=v[0],ans2=v[0];
    for (long long int i = 1; i < n; i++) 
    {   
        ans2=gcd(ans2,v[i]);
        g=gcd(v[i], ans);
        ans = (((v[i]*ans))/g); 
    }
    k->gcd=ans2;
    k->lcm=ans;
    return k; 
} 
int main()
{
	long long int sizev;
    cout<<"Please enter the size of an array:-"<<endl;
    cin>>sizev;
    cout<<"Please enter the elements:-"<<endl;
    vector<long long int> v;
    for(long long int i=0;i<sizev;i++)
    {
      long long int value;
      cin>>value;
      v.push_back(value); 
    }
    struct answer * p=findlcm(v,sizev);
    cout<<"The LCM of the array is:- "<<p->lcm<<endl;
    cout<<"The GCD of the array is:- "<<p->gcd<<endl;
	return 0;
}
