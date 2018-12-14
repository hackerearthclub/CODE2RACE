r1=int(input("Please enter the starting number: "))
r2=int(input("Please enter the ending number: "))
for i in range(r1,r2+1):
  if(i%3==0 and i%5!=0):
    print("Fizz")
  elif(i%3!=0 and i%5==0):
    print("Buzz")
  elif(i%3==0 and i%5==0):
    print("FizzBuzz")
  else:
    print(i)
