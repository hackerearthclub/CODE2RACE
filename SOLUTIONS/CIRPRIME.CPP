#include<iostream.h>
#include<conio.h>
#include<math.h>
int CheckPrime(int n)
{
//int flag=0;
  for(int i=2; i<=n/2; i++)
  {
	if(n%i==0)
	{  return 0;
	}
  }
  return 1;
}

int CircularPrime(int n)
{
  int flag1=n;
  int check=1;
  int count=0,	flag2=0,   sum=0;

while(flag1)
 {  flag1=flag1/10;
  count++;
 }

flag1=n;


while(check==1)
  {
	check=CheckPrime(flag1);
	flag2=flag1%10 ;
	flag1=(flag1/10)+(flag2*pow(10,count-1));
	if((flag1==n)&&(check==1))
	{
	return n;
	}
  }


return 0;


}

void main()
{ long int num,sum=0;
	int check=0;
cout<<"Enter the input integer:\t";
cin>>num;

for(int i=1; i<=num; i++)
	{
	   check=CircularPrime(i);
	   cout<<check<<"\t  ";
	   sum=sum+check;

	}
  cout<<sum-1;

  getch();
}