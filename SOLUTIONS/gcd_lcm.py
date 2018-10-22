# Python version of C++ Solution in GeeksforGeeks
def gcd(a,b):
	if a == 0:
		return b
	return gcd(b%a,a)

def findGCD(_list,n):
	res = _list[0]
	for i in range(1,n):
		res = gcd(_list[i], res)

	return res

def findLCM(_list,n):
	res = _list[0]
	for i in range(1,n):
		res = ((_list[i] * res) /(gcd(_list[i],res)))

	return res


if __name__ == '__main__':
	_l = [ 1, 2, 3]
	n = len(_l)
	res = findGCD(_l,n)
	print("GCD=	" + str(res))
	res = findLCM(_l,n)
	print("LCM=	" + str(res))
