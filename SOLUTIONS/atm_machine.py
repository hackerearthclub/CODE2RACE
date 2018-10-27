n=int(input())
for  i in range(0,n):
    k,n=map(int,input().split())
    l=list(map(int,input().split()))
    l1=[]
    for j in l:
        p=n-j
        if(p>=0):
            l1.append("1")
            n=p
        else:
            l1.append("0")
    print("".join(l1))        
            
