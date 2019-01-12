def _lcm(a,b):
  if(a>b):
    num=a
    den=b
  else:
    num=b
    den=a
  rem=num%den
  while(rem!=0):
    num=den
    den=rem
    rem=num%den
  gcd=den
  lcm=int(int(a*b)/int(gcd))
  return lcm
def _gcd(c,d):
  while(d):
    c,d=d,c%d
    return c
l=[2,4,6,8,10]
a=l[0]
b=l[1]
lcm=_lcm(a,b)
for i in range(2,len(l)):
  lcm=_lcm(lcm,l[i])
print(lcm)
c=l[0]
d=l[1]
gcd=_gcd(c,d)
for i in range(2,len(l)):
  gcd=_gcd(gcd,l[i])
print(gcd)
