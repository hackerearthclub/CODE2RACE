#include<iostream>
#include<math.h>

using namespace std;
#define MAX 25
// Here the Sudoku is solved using backtracking 
// The time complexity of backtracking is N^M 
// Here N: Number of possibilities for each square
// M: Number of Spaces that are blank
int Sudoku[MAX][MAX],size;

// Function to Enter the values of Sudoku initially
void EnterSudoku(){
	
	cout<<"Enter the size of the sudoku board\n";
	cin>>size;
	assert(size<=25);
	cout<<"Enter the board at its present state\n";
	cout<<"Enter '0' for blank\n";
	for(int i=0;i<size;i++){
		for(int j=0;j<size;j++){
			cin>>Sudoku[i][j];
		}
	}
}

// Function to display the solved Sudoku 
void displaysolved(int Sudoku[MAX][MAX], int size){
	
	for(int i=0;i<size;i++){
		for(int j=0;j<size;j++){
			cout<<Sudoku[i][j]<<" ";
		}
		cout<<"\n";
	}
}

// Function to check if the Sudoku is solved or not
bool isSolved(int Sudoku[MAX][MAX], int size){
	
	for(int i=0;i<size;i++)
	{
		for(int j=0;j<size;j++){
			if(Sudoku[i][j]==0)
			return false;
		}
	}
	return true;
}

// Function to calculate if a number can be filled at (i,j)
// depending on the numbers filled in ith row , jth column 
// and the block in which (i,j) is present

int possibilities(int Sudoku[MAX][MAX], int size, int A[], int row, int col){
	
	int count = 0;
	int size_of_block = (int)sqrt(size);
	bool checked[MAX+1] = {false};
	
	// Note no.s appeared in current row
	
	for(int i=0;i<size;i++){
		checked[Sudoku[row][i]] = true;
	}
	
	// Note no.s appeared in current column
	
	for(int i=0;i<size;i++){
		checked[Sudoku[i][col]] = true;
	}
	
	// Note no.s appeared in current block
	
	row = (row/size_of_block)*size_of_block, col = (col/size_of_block)*size_of_block;
	for(int i=row;i<row+size_of_block;i++){
		for(int j=col;j<col+size_of_block;j++){
			checked[Sudoku[i][j]] = true;
		}
	}

	//Filling Array A with numbers which are not appeared in rows,columns and blocks of (i,j)
	for(int i=1;i<=size;i++){
		if(!checked[i]){
			A[count++] = i;
		}
	}
	return count;

}

// Function to solve Sudoku board using Backtracking
// This returns solved_flag true if atleast one solution is possible, false otherwise
// This is the key function which solves the board
// Initially it checks if the board is solved or not
// If the board is not full it checks first position/cell which is vacant
// Then it finds possible values at that position
// It tries all the possible values at that position
// For each trial/guess/choice, it tries to solve the updated board
// If no choice come out to be correct one for that vacant place, then definitely
// some previous choices are wrong, Hence it backtracks and tries to correct the previous choices.


void SolveSudoku(int Sudoku[MAX][MAX], int size, bool &solved_flag){
	int A[MAX+1] = {0}, n = 0;
	// Check if the sudoku is already solved?
	// If YES then display the sudoku
	if(isSolved(Sudoku,size)){
		if(solved_flag){
			cout<<"Sudoku Solved Successfully!\n";
		}
		solved_flag = true;
		// Show the solution
		cout<<"THE SOLUTION IS \n";
		displaysolved(Sudoku,size);
	}
	else
	{
		//Find first vacant place/position
		int break_flag = 0;
		int row = 0,col = 0;
		for(int i=0;i<size;i++){
			for(int j=0;j<size;j++){
				if(!Sudoku[i][j])
				{
					break_flag = 1;
					row = i;
					col = j;
					break;
				}
			}
			if(break_flag){
				break;
			}
		}
		// check possibilities at that vacant place
		n = possibilities(Sudoku,size,A,row,col);
		for(int i=0;i<n;i++){
			// Put value at vacant place (row,col)
			Sudoku[row][col] = A[i];
			//Now solve the updated board
			SolveSudoku(Sudoku,size,solved_flag);

		}
		// Put any value does not solves our board implies that we must have made wrong choice earlier
   // so we make this Sudoku[row][col] again a vacant cell and try to correct our previous guesses/choices.
   Sudoku[row][col] = 0;
	}
}


int main(){
	// For fast input and output
	ios_base::sync_with_stdio(false); cin.tie(0);
	// For input and output file
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	EnterSudoku();
	bool solved_flag = false;
	//Processing
    cout<<"Finding Solutions!\n\n"<<endl;
    SolveSudoku(Sudoku, size, solved_flag);
    if(!solved_flag){
    	cout<<"INVALID BOARD!!\n";
    }
    else
    {
    	cout<<"EXIT\n";
    }
}