def calculate(n):
    t1 = 0
    t2 = 0
    for x in range(n+1):
        t1 += x*x
    for x in range(n+1):
        t2 += x
    t2 = t2*t2
    return t2-t1

line1 = int(input("How many test cases do you have?"))
list1 = []
for x in range(line1):
    n = int(input("Enter an integer"))
    list1.append(n)
for x in range(line1):
    print(calculate(list1[x]))
