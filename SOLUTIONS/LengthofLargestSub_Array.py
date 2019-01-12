import math

arr0 = [4,7,4,7,11,5,4,4,4,5]
arr1 = [1,9,3,4,5,6,7,8]
arr2 = [2,3,4,4,3,3,4]
arr3 = [1,2,1,2,3,1,1,1,2,2,2]
arr4 = [1,2,2,3,4,4,4,4]
arr5 = [27, 3, 4, 2, 2, 1, 3, 5, 49]
arr6 = [2, 3, 4, 5, 6, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]

def count_prime (num):
	new_num = math.sqrt(num)
	if num % 2 == 0:
		if num != 2:
			return 'non_prime'
		return 'prime'
	if num != 3 and num % 3 == 0:
		return 'non_prime'
	if num == 1:
		return 'non_prime'
	if int(new_num) == new_num:
		return 'non_prime'
	else:
		return 'prime'

def get_largest(arr):
	non_prime = 0
	prime = 0
	largest = 0
	compare = 0
	
	for a,y in enumerate(arr):
		num_type = count_prime(y)
		if num_type == 'non_prime' and prime > 0:
			non_prime += 1
			if non_prime < prime:
				if a < (len(arr)-1):
					largest += 1
				if non_prime + 1 != prime and a == (len(arr) - 1):
					largest += 1
			if non_prime == prime:
				if a == (len(arr)-1):
					return largest if largest > compare else compare
				if count_prime(arr[a+1]) == 'prime':
					largest += 1
				else:
					compare = largest
					non_prime = 0
					prime = 0
					largest = 0
			if non_prime > prime:
				compare = largest
				non_prime = 0
				prime = 0
				largest = 0
		if num_type == 'prime':
			prime += 1
			largest += 1
	return largest if largest > compare else compare

#print(True if get_largest(arr0) == 9 else False)
#print(True if get_largest(arr1) == 5 else False)
#print(True if get_largest(arr2) == 7 else False)
#print(True if get_largest(arr3) == 5 else False)
#print(True if get_largest(arr4) == 5 else False)
#print(True if get_largest(arr5) == 8 else False)
#print(True if get_largest(arr6) == 20 else False)
