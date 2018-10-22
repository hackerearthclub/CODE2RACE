from functools import reduce
inp = input()
print (reduce(lambda x, y: x*y, [ord(ch) for ch in inp], 1))