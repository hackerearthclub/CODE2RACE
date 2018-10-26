def binary_multiple(number):
    x = int(number,2)
    if x%3 == 0:
        return 1
    else:
        return 0

test = int(input("Enter the number of test cases"))
list1 = []
while test < 1 or test > 100:
    print("Number of test cases must be between 1 and 100")
    test = int(input("Enter the number of test cases"))
for x in range(test):
    y = input("Enter the binary number")
    while len(y) < 1 or len(y) > 100:
        print("Length of input string must be between 1 and 100")
        y = input("Enter the binary number")
    list1.append(y)
for x in range(test):
    print(binary_multiple(list1[x]))
