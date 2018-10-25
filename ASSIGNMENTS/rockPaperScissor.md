Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

* Rock beats scissors

* Scissors beats paper

* Paper beats rock
#include <iostream>

using namespace std;
``` C
int main()
{
	char k1, k2;
	cout << "Welcome to RPS\n";
	cout << "What's your choose player 1(R - P - S): ";
	cin >> k1;
	cout << '\n';
	cout << "What's your choose player 2(R - P - S): ";
	cin >> k2;
	cout << '\n';
	if (k1 == k2) cout << "DRAW";
	else if ((k1 == 'R' && k2 == 'S') || (k1 == 'S' && k2 == 'P') || (k1 == 'P' && k2 == 'R')) cout << "Congrat player 1, you won !!!";
	else cout << "Congrat player 2, you won !!!";
}
```
