c=(10**9)+7
for _ in range(int(input())):
	
	A,B,N=map(int,input().split())
	su=0
	for i in range(1,N+1):
		x=A**i-B**i
		for j in range(1,N+1):
			b=A**j-B**j
			a=x
			if a<b:
				temp=a
				a=b
				b=temp
			
			l=b
			b=(pow(A,i,b)-pow(B,i,b))%b
			a=l
			
			while(b>0):
				a,b=b,a%b
			
			su+=a%c
	print(su)
			
