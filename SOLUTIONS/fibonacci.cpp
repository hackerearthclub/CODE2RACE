#include<iostream.h>
void main()
{
	int a=0,b=1,n,d=0;
	cout<<"how many terms of fibonacci series to display";
	cin>>n;
	for(int i=1;i<=n;i++)
	{
	if(i==1)
	cout<<a<<" ";
	if(i==2)
	cout<<b<<" ";
	d=a+b;
	a=b;
	b=d;
	cout<<d<<" ";
	}
}