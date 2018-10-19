n = int(input('Number of Capacitors: '))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def countCap(n):
    x = factorial(n) + 1
    return x


print(countCap(n))
