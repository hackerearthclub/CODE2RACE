#include <iostream>

using namespace std;

int main()
{
  int arr[100],n,i,flag;
  cout<<"Enter the size of the array."<<endl;
  cin>>n;

  cout<<"Enter the array elements."<<endl;
  for(i=0; i<n; i++)
  {
      cin>>arr[i];
      cout<<endl;
  }

  for(i=0; i<n; i++)
  {
      if(arr[0] == arr[i])
      {
          flag=0;
      }
      else
      {
          flag=1;
          break;
      }
  }

  if(flag==0)
  {
      cout<<"UNIFORM!!!";
  }

  else if(flag!=0)
  {
      cout<<"Differences detected";
  }
  return 0;
}
