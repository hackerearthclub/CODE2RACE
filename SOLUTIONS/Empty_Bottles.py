for _ in range(int(input())):
	n=int(input())
	b_h=list(map(int,input().split()))
	s=0
	c=0
	
	for a in b_h:
		if a==100:
			c=c+1
		else:
			s=s+a
			
	filled_bottle=c+s//100
	
	print(filled_bottle)
