// C++ code to find Even Fibonacci 
//Series using normal Recursion 
#include<iostream> 
using namespace std; 

// Function which return 
//nth even fibonnaci number 
long int evenFib(int n) 
{ 
	if (n < 1) 
	return n; 
	if (n == 1) 
	return 2; 

	// calculation of 
	// Fn = 4*(Fn-1) + Fn-2 
	return ((4 * evenFib(n-1)) + 
			evenFib(n-2)); 
} 

// Driver Code 
int main () 
{ 
	int n;
  cin>>n;
  for(i=0;i<n;i++)
  {
	cout << evenFib(n);
  cout<<endl;
  }
	return 0; 
} 
