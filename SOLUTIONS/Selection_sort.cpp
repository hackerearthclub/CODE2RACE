#include<iostream>
using namespace std;
template <class t>

void sel_sort(t arr[],int n )
{    t temp;

 for(int j=0;j<n;j++)
  {     t small=arr[j];
     int pos =j;  
 for(int k=j+1;k<n;k++)          // calculate smallest element in the array
   {   if(arr[k]<small)
              {
			  small=arr[k]; pos=k;}     
	}
	temp=arr[j];       //swapping smallest element and the first element
	arr[j]=small;
	arr[pos]=temp;
	
 	
 }



}






int main()
{ int n;
cout<<"Enter the no. of elements"<<endl;
       cin>>n;
       
string arr[n];	     
for(int i=0;i<n;i++)
cin>>arr[i];
sel_sort(arr, n);
cout<<"The sorted array is ";
for( int s=0;s<n;s++)
{ cout<<arr[s]<<" ";
}

}
