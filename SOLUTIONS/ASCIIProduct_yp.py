var= raw_input()
lvar= list(var)
x=1
for a in range(1, len(lvar)+1):
  x= x*ord(lvar[a-1])
 print (x)
