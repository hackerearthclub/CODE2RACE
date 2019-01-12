#include<iostream>
using namespace std;

int main()
{
    int num,count=0,b;
    cout<<"Enter the number: ";
    cin>>num;
    //Counting number of zeros in factorial of the number inputted..
    if(num>=5)
    {
        for(int i=5;i<=num;i++)
        {
            if(i%5==0)
            {
                count++;
                b=i/5;
                while((b%5)==0)
                {
                    count++;
                    b/=5;
                }
            }
        }
    }

    if(count == 0)
    {
        cout<<"There are no zeros!";
    }
    else
    {
    cout<<"The number of zeros are: "<<count;
    }
    return 0;
}
