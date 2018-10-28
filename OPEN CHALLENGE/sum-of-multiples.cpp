#include<iostream>
using namespace std;
int main()
{
  int var=0, i;
  for(i=3; i<1000; i++)
  {
    if(i%3 == 0 && i%5 == 0)
      var = var+i;
    else if(i%3 == 0)
      var = var+i;
    else if(i%5 == 0)
      var = var+i;
  }
  cout<<var;
  return 0;
}
