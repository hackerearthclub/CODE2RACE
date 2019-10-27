def bubbleSort(n):
	for num in range(len(n)-1,0,-1):
    	for i in range(num):
        	if (n[i]>n[i+1]):
            	t = n[i]
            	n[i] = n[i+1]
            	n[i+1] = t
a = int(input("Enter number of elements to enter in array: "))
n = list(map(int, input("Enter Numbers in Array: ").split(",", a)[:a]))
bubbleSort(n)
print("Sorted in Ascending order",n)
