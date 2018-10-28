import sys
tc=int(sys.stdin.readline())
ans=[]
list1=[]
results=[]
for i in range(0,tc):
    k=int(sys.stdin.readline())
    list1=sys.stdin.readline().split()
    results = list(map(int, list1))
    count=0
    for j in results:
        if(j%2==0):
            count=count+1
    ans.append(count)
    
    
for i in ans:
    print(i)
