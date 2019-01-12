try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3
a=str(raw_input("player 1"))
b=str(raw_input("player 2"))
print("select an option")
print("1.rock 2.paper 3.scissors")
c=int(raw_input("a: "))
d=int(raw_input("b: "))
if(a==1):
  if(b==2):
    print("b won")
  elif(b==3):
    print("a won")
elif(a==2):
  if(b==1):
    print("a won")
  elif(b==3):
    print("b won")
else:
  if(b==1):
    print("b won")
  elif(b==2):
    print("a won")
