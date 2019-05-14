import numpy 
T=int(input("No.of Test Cases"))
s=input()
l=s.split()
for i in range (0,T):
    for j in range (1,int(l[i])+1):
        count=0
        if(j%15==0):
            print("FizzBuzz")
            count=1
        else:
            if(j%3==0):
                print("Fizz")
                count=1
            if(j%5==0):
                print("Buzz")
                count=1
        if(count==0):
            print(j)
        
