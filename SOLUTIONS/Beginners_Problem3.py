a=int(input())
for i in range(a):
  b=int(input())
  c=len([x for x in list(map(int,input().split())) if x%2==0])
  print(c)
