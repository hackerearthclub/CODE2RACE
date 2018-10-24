import math

def isPrime(number): #number is an int
    for i in range(2,int(math.sqrt(number)+1)):  #It's only needed to look until sqrt of the number (included, so +1)
        if (number%i == 0):
            return False
    return True


def rotationsOf(numberString): #number is a string representing a number
    possibilities = []
    for i in range(len(numberString)-1):
        numberString = numberString [1:] + numberString[0]
        possibilities.append(numberString)
    return possibilities


def isCircularPrime(numberString):
    for num in rotationsOf(numberString):
        if (not isPrime(int(num))):
            return False
    print(numberString)
    return True

def sumOfCircularPrimesBelow(numberString):
    sum = 0
    for i in range(2, int(numberString)):
        if (isPrime(int(i))):
            if (isCircularPrime(str(i))):
                sum = sum + i
    return sum




numberString = input("Please type a number: ")
print(sumOfCircularPrimesBelow(numberString))
