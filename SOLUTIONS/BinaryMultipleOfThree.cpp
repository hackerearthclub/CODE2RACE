#include <iostream>
using namespace std;

# I defined my own function to calculate power of an integer
# Instead of using cmath library
int calculate_power(int base, int exponent){
	int result = 1;
	for(int i=0;i<exponent;i++){
		result *= base;
	}
	return result;
}

int BinaryToDecimal(string binary){
	int exponent=0;
	int decimal_number=0;
	for(int i=binary.length()-1;i>=0;i--){
		if(binary[i] == '1'){
			decimal_number +=  calculate_power(2,exponent);
		}
		exponent++;
	}
	return decimal_number;
}


int main() {
	int T;
	string binaryString;;
	cin>>T;
	for(int t=0;t<T;t++){
		cin>>binaryString;
		int number=BinaryToDecimal(binaryString);
		if(number%3 == 0){
			cout<<1<<endl;
		}
		else{
			cout<<0<<endl;
		}
	}
	return 0;
}
