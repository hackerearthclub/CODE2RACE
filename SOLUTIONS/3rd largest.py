Arr = list(map(int, input("enter numbers separated by space = ").split()))

Max1 = Max2 = Max3 = min(Arr)

for x in range(1, len(Arr)):
	if(Arr[x] > Max1): Max1, Max2, Max3 = Arr[x], Max1, Max2
	elif(Max1 >= Arr[x] > Max2): Max2, Max3 = Arr[x], Max2
	elif(Max1 >= Max2 >= Arr[x] > Max3): Max3 = Arr[x]

print("third Max = ", Max3)
