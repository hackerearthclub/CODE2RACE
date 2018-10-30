n1 = [20, 10, 30, 10, 20, 30]
n2 = [30, 20, 10, 30, 20, 50]
n1.soft()
n2.soft()
if compare(n1,n2)==True:
    print("Equal")
else:
print("Not Equal")