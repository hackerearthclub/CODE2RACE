from functools import reduce

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

def lcm(a, b):
	return a*b // gcd(a, b)

# finding lcm
# p = [1, 2, 8, 3]
p = [2, 7, 3, 9, 4]

print (reduce(lambda x, y: lcm(x, y), p))

# finding gcd
q = [1, 2, 3]
# q = [2, 4, 6, 8]

print (reduce(lambda x, y: gcd(x, y), q))