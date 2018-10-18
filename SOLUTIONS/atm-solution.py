t = int(input())

for _ in range(t):
	n,curr_val = [int(x) for x in input().split()]
	req = [int(x) for x in input().split()]
	result_str = ""
	for i in range(len(req)):
		#if value available append 1 and subtract from curr_value
		if req[i] <= curr_val:
			curr_val -= req[i]
			result_str += '1'
		#if curr_value is 0, append 0 for all remaining values
		elif curr_val == 0:
			result_str += '0'*(n-i)
			break
		else:
			result_str += '0'
	print(result_str)