#include<iostream>
using namespace std;
int main()
{
    int n,temp,sum=0,r;
    cout<<"Enter the number to be checked"<<endl;
    cin>>n;
    temp = n;
    while(n>0)
    {
        r = n%10;
        sum += (r*r*r);
        n /=10;
    } 
    if(sum == temp)
    {
        cout<<"Number is armstrong"<<endl;
    }
    else{
        cout<<"Not an Armstrong Number"<<endl;
    }
    return 0;
}