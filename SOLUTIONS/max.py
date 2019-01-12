t = int(input())
ans = []
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    sum = sum(l)
    m = int(sum/100)
    ans.append(m)

for i in range(len(ans)):
    print (ans[i])
