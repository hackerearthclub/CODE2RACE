T=int(input())
for _ in range(T):
    N,a,b=map(int,input().split())
    l=[0]
    i=N
    j=0
    while i!=0:
        l.extend([i*a-m*(a+b) for m in range(i+1)])
        i-=1
    l=list(set(l))
    print(len(l))