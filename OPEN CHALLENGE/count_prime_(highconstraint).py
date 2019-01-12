major=[0 for i in range(10**6+29)]
def SieveE(n):
    prime=[True for i in range(n+1)]
    p=2
    while p*p<=n:
        if prime[p]:
            for i in range(p*2,n,p):
                prime[i]=False
        p+=1
    c=0
    major[0]=0
    major[1]=0
    for i in range(2,n):
        if prime[i]:
            c+=1
            major[i]=c
        else:
            major[i]=c

SieveE(10**6+29)
for _ in range(int(input())):
    a,b=map(int,input().split())
    print(major[b]-major[a-1])
