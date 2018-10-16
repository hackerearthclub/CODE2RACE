import math

arr0 = [4,7,4,7,11,5,4,4,4,5]
arr1 = [1,9,3,4,5,6,7,8]
arr2 = [2,3,4,4,3,3,4]
arr3 = [1,2,1,2,3,1,1,1,2,2,2]

def count_prime (num):
	new_num = math.sqrt(num)
	if num % 2 == 0:
		if num != 2:
			return 'non_prime'
		return 'prime'
	if num == 1:
		return 'non_prime'
	if int(new_num) == new_num:
		if num % new_num == 0:
			return 'non_prime'
	else:
		return 'prime'

def get_largest(arr):
	non_prime = 0
	prime = 0
	largest = 0
	for a,y in enumerate(arr):
		num_type = count_prime(y)
		if num_type == 'non_prime' and prime > 0:
			non_prime += 1
			if non_prime <= prime and a < (len(arr)-1):
				largest += 1
			if non_prime > prime:
				non_prime = 0
				prime = 0
				largest = 0
		if num_type == 'prime':
			prime += 1
			largest += 1
	return largest
	
print(get_largest(arr3))
			
