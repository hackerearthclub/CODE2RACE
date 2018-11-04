a=int(input())
ans=[]
while(a!=0):
  n=int(input())
  s=0
  l=list(map(int,input().split()))
  for i in range(len(l)):
    if(l[i]%2==0):
      s+=1
  ans.append(s)
  a-=1
for i in range(len(ans)):
  print(ans[i])
