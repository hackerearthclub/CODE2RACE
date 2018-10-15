#include <iostream>
#include <cstdlib>

using namespace std;

int matrix [3][3] = {
    //R P S -- 1St player
     {0,2,1},// R
     {1,0,2},// P
     {2,1,0} // S -- 2Nd player
};

void clear_screen()
{
// https://stackoverflow.com/questions/228617/how-do-i-clear-the-console-in-both-windows-and-linux-using-c
#ifdef _WIN32
    // windows
    std::system("cls");
#else
    // unix & linux
    std::system("clear");
#endif
}

bool validateINP(int x){
    if(x != 1 && x != 2 && x != 3) return true;
    return false;
}

void startGame(){
    int A, B;
    //
    do{
        cout  <<    "First player choice (input number only):\n"
                    "1. Rock\n"
                    "2. Paper\n"
                    "3. Scissors"  <<  endl;
        cin  >>  A;
    }while(validateINP(A));
    A--;
    //
    clear_screen();
    //
    do{
        cout  <<    "Second player choice (input number only):\n"
                    "1. Rock\n"
                    "2. Paper\n"
                    "3. Scissors"  <<  endl;
        cin  >>  B;
    }while(validateINP(B));
    B--;
    //
    switch(matrix[A][B]){
        case 0: cout << "Draw!" << endl;
                break;
        case 1: cout << "First player wins!" << endl;
                break;
        case 2: cout << "Second player wins!" << endl;
                break;
    }
}

int main(){
    bool cont = true;
    string inp;
    do{
        clear_screen();
        startGame();
        while(true){
            cout << "Play again?: (Yes/No/Y/N)" << endl;
            cin >> inp;
            if(inp=="Yes"||inp=="No"||inp=="Y"||inp=="N"||inp=="yes"||inp=="no"||inp=="y"||inp=="n"){
                if(inp=="No"||inp=="N"||inp=="no"||inp=="n") cont = false;
                break;
            }else{
                cout << "Please input again";
            }
        }
    }while(cont);
    return 0;
}
