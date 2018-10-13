#include<cstdio>

using namespace std;

int main() {
	int T;
	scanf("%d" ,&T);

	while(T--) {
		long long N;
		scanf("%lld" ,&N);

		long long sumOfSquare = 0;
		long long squareOfSum = 0;

		for(long long i = 1; i <= N; i++) {
			sumOfSquare += i*i;
			squareOfSum += i;
		}

		squareOfSum *= squareOfSum;

		long long difference = squareOfSum - sumOfSquare;
		printf("%lld\n" ,difference);

	}
}