#Even fibonacci numbers
def ev_fibo(n):
 for i in range(0,n):
  first=1
  second=1
  Sum =0
  third = 0
  m=int(input())
  while third<=m:
     third= first+second
     if third%2==0:
       Sum+=third
     first=second
     second=third
  print(Sum)
n=int(input())
ev_fibo(n)

