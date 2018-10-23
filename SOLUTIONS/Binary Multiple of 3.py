n=int(input())
l=[]
for i in range (n):
    l.append(input())
for i in l:
    odd=0
    even=0
    for k in range(len(i)):
        if((k%2==1)and(i[k]=='1')):
            odd+=1
        elif((k%2==0)and(i[k]=='1')):
            even+=1
    if((odd-even)==0):
        print(1)
    else:
        print(0)
