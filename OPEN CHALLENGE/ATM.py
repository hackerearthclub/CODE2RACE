def appendstring(t,n,k,arr):
	binarystring = []
	for i in range(0,t):
		for j in range(0,n):
			if(arr[j] <= k):
				binarystring.append(1)
				k=k-arr[j]
			else:
				binarystring.append(0)

	x = "".join(str(x) for x in binarystring)
	print(x)







t = int(input("input the testcases"))
n = int(input("Enter the elements of array:"))
k = int(input("the amount"))
arr = [0] * n
for c in range(0, n):
	arr[c] = int(input())

appendstring(t,n,k,arr)