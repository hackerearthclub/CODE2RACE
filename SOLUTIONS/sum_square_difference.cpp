#include<iostream.h>
void main()
{
	int a,b,t,n;
	cin>>t>>n;
	while(t>0)
	{
		a=(n*(n+1))/2;
		b=(n*(n+1)*(2*n+1))/6;
		if(a>b)
		cout<<a-b;
		else
		cout<<b-a;	
	t--;
	}
}