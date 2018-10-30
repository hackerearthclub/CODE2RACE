#include <iostream>
# include <vector>

using namespace std;

int main()
{
    int tests;
    cin >> tests;
    
    while (tests --){
        
        long int n;
        cin >> n;
        vector <long long int > marks,  solution ;
        
        marks.resize(n);
        solution.resize(n);
        
        for ( int i = 0 ; i < n ; i ++)
            cin >> marks[i];
        
        solution[0] = marks [0];
        
        solution[1] = max ( marks[1], marks[0]);
        
        
        for ( int i = 2 ; i < n ; i ++)
            solution[i] = max ( solution[i-2] + marks[i], marks[i-1] );
            
        cout << marks[n-1] << endl;
            
    }
    
return 0;
}
