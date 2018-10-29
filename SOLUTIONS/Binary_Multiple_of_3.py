


ntcases = int(input("Please type the number of test cases: "))
for i in range(ntcases):
    binaryString = input("Please type a binary number: ")
    exp = 0
    result = 0
    for bit in binaryString:
        result += int(bit)*(2**exp)
        exp = exp+1
    if (result%3 == 0):
        print("1")
    else:
        print("0")
        