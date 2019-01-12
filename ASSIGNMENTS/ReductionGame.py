#Author: Nirupam Gunwal

# Issue Solve Reduction Game #573

#Detailed Solution to the Problem Described at https://github.com/hackerearthclub/CODE2RACE/blob/master/ASSIGNMENTS/Reduction%20Game.md
# in Python 3



def answer(arr):

	ntestcase = arr[0]

	narr = []
	k = []
	sumfinal = []
	

	arrn = []
	loopcount = len(arr)
	i = 1
	while i < loopcount :
		
		n = arr[i]
		narr.append(n)
		k.append(arr[i+1])
		arrlist = arr[i + 2 : i + n + 2]
		arrn.append(arrlist)
		i = i + n + 2
		
		
	for i in range(ntestcase):
		sortedarray = sorted(arrn[i])
		
		j = 0
		while j < len(sortedarray) - 1:

			while min(sortedarray[j],sortedarray[j+1]) > k[i]:
				sortedarray[j] = sortedarray [j] - 1
				sortedarray[j+1] = sortedarray [j+1] - 1

			j = j + 1	

		sumfinal.append(sum(sortedarray))	


	print("Output:")
	print(sumfinal)


def main():

	print("Use Test Case OR Input Your Own .(y for Your Own Input else Test Case will be considered)")

	if(str(input()) == 'y'):
		print("Test Case Selected")
		arr = [3,2,1,1,2,2,1,2,2,3,1,2,3,2]

	else:

		print("Input Selected .Give the input according to the question and use dont use spaces to seperate numbers :")
		print(" Input Should be of the format like this : 32112212231232 (No spaces)")
		arr = list(input())

		for i in range(len(arr)):
			arr[i] = int(arr[i])


	answer(arr)		

if __name__ == '__main__':
	main()			
	
