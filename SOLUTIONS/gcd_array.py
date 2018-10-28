def hcf(a,b): 
  if(b==0): 
    return a 
  else: 
    return hcf(b,a%b) 

a = list(map(int, input().split()))
gcd = 0
if len(a)==2:
 gcd = hcf(a[0] ,a[1])
else:
  gcd = hcf(a[0] ,a[1])
  for i in range(2, len(a)):
    gcd = hcf(gcd, a[i])

print(gcd)
