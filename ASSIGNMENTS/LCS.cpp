#include <iostream>

using namespace std;

int main(int argc, char** argv) {
	
	int s1[] = {1, 0, 1, 1, 0};		// m = 5
	int s2[] = {0, 1, 0, 0, 1, 0}; 	// n = 6
	
	
	int arr[6][7];
	string dir[6][7];
	
	for(int i = 0; i < 6; i ++) {
		for(int j = 0; j < 7; j++) {
			arr[i][j] = 0;
		}
	}
	
	for(int i = 1; i < 6; i ++) {
		for(int j = 1; j < 7; j++) {
			if(s1[i-1] == s2[j-1]) {
				arr[i][j] = arr[i-1][j-1] + 1;
				dir[i][j] = "diagonal";
			} else {
				if(arr[i][j-1] == arr[i-1][j]) {
					arr[i][j] = arr[i][j-1];
					dir[i][j] = "both";
				} else if(arr[i][j-1] > arr[i-1][j]) {
					arr[i][j] = arr[i][j-1];
					dir[i][j] = "left";
				} else {
					arr[i][j] = arr[i-1][j];
					dir[i][j] = "up";
				}
			}
		}
	}
	
	for(int i = 1; i < 6; i ++) {
		for(int j = 1; j < 7; j++) {
			cout << arr[i][j] << " ";
		}
		cout << endl;
	}
	
	for(int i = 1; i < 6; i ++) {
		for(int j = 1; j < 7; j++) {
			cout << dir[i][j] << " ";
		}
		cout << endl;
	}
	
	return 0;
}
