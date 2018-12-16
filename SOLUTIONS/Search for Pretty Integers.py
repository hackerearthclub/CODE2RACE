aa, bb = map(int,raw_input().split())

a = map(int,raw_input().split())
b = map(int,raw_input().split())

ma = min(a)

mu = 1000000
mb = min(b)

for i in b:
	if i in a and i<mu:
		mu = i

if mu == 1000000:
	if ma<mb:	
		print str(ma) + str(mb)
	else:
		print str(mb) + str(ma)
else:
	print mu
