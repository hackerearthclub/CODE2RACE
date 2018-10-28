'''input
1
2...2
'''
t=int(input())
for i in range(t):
    s=input()
    a=[0]*len(s);n=len(s)
    for i in range(len(s)):
        if s[i]!='.':
            for i in range(max(0,i-int(s[i])),min(n,i+int(s[i])+1)):
                a[i]+=1
    for i in a:
        if a[i]>1:
            print('unsafe')
            break
    else:
        print('safe')
