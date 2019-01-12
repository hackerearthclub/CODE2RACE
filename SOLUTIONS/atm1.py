t=int(input())
while t>0:
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    
   
    for i in a:
        if k>=i:
            print('1',end="")
            k=k-i
        else:
            print('0',end="")
    print('\r')        
    t=t-1  
