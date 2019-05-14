//to check whether string is pallindrome or not
#include<iostream>
#include<cstring>
using namespace std;
int main()
{string str,str2;
cout<<"Enter the string :";
getline(cin,str);
int l,i;
l=str.size();
for(i=l-1;i>=0;i--)
{ str2=str2+str[i];
}
cout<<str2<<endl;
if(!str.compare(str2))
 cout<<"The given string is Pallindrome";
else
 cout<<"The given string is not pallindrome";
}

