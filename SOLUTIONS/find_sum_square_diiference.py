#code
t=int(input())
while t>0:
	x=int(input())
	s1=0
	s2=0
	i=1
	while i<=x:
		s1=s1+i
		s2=s2+i**2
		i=i+1
	print(abs(s1**2-s2))
	t=t-1
