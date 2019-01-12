# solution for issue #472
# Get number of test cases
n = int(input("Enter the number of cases: "))

# iterate cases
for i in range(n):
    # get input number as string, convert to binary using int(number, base)
    number = int(input(), 2)
    # check if number is a multiple of three
    if number%3 == 0:
        print(1)
    else:
        print(0)
