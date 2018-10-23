def tester():
    try:
        testCases = int(input("How many test cases? "))
    except ValueError:
        print("Please choose an integer.")

    for  i in range(testCases):
        binaryNum = input("Choose a binary number: ")
        testBinary = binaryToDecimal(binaryNum)
        if (testBinary % 3 == 0):
            print("1")
        else:
            print("0")


def binaryToDecimal(binary):
    """Convert binary number to decimal number.

    >>> binaryToDecimal (255)
    11111111

    Params:
    """
    try:
        binary = int(binary)
        decimal = 0
        i = 0
        while (binary != 0):
            dec = binary % 10
            decimal = decimal + dec * 2 ** i
            binary = binary // 10
            i += 1
        return decimal
    except ValueError:
        print("Oops something went wrong! Try another input.")
        tester()
    except TypeError:
        print("Check your inputs.")
        tester()

tester()
