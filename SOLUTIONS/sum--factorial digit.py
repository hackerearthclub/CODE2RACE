import math
t=int(input())
while t>0:
	x=int(input())
	number=math.factorial(x)
	s=sum(int(digit) for digit in str(number))
	print(s)
	t=t-1
	
	
	
