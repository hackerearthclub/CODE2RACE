t = int(input())  # read a line with a single integer
for i in range(1, t +1):
	n = int(input())
	A = [int(s) for s in input().split(" ")] 
	c= 0 # read a list of integers, 2 in this case
	for x in range(0, n):
		if(A[x]%2==0):
					c=c+1
	print(c)
