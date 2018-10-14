import math
T = input()

while(T > 0):
	T = T-1
	N = input()
	print(sum(map(int, str(math.factorial(N)))))