for _ in range(int(input())):
	n=int(input())
	botle_height=list(map(int,input().split()))
	s=0
	c=0
	
	for x in botle_height:
		if x==100:
			c+=1
		else:
			s+=x
			
	filled_bottle=c+s//100
	
	print(filled_bottle)
