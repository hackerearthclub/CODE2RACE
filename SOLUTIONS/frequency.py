c=int(input("enter number of test cases: "))
for i in range(0,c):
    n=int(input("number of values :"))
    x=input(("enter all values : "))
    x=(x.split(" "))
    frequency=0
    for j in range(n):
        if x[i]%2==0:
            frequency=frequency+1
    print(frequency)
