//reversing of array
#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

void rev(int t[], int left, int right)
{
	int temp;
	if(right>left)
	{
		temp=t[left];
		t[left]=t[right];
		t[right]=temp;
		rev(t, left+1,right-1);
	}
}

void display(int array[], int sizeArray)
{
	for(int i=0;i<sizeArray;i++)
	{
		cout << array[i] << " ";
	}	
}

int main()
{
	int arrayOfInteger[]={2,3,3,5,6,1,8,5,7,4,8,0,1,4,3,6,8,9,3,3,2,0,6};
	int sizeA = sizeof(arrayOfInteger)/sizeof(int);
	display(arrayOfInteger, sizeA);
	cout << endl;
	rev(arrayOfInteger, 0, sizeA-1);
	display(arrayOfInteger, sizeA);
		
}
