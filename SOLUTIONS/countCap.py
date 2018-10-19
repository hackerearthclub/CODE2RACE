n = int(input('Number of Capacitors: '))

def countCap(n):
    if n == 0:
        return 1
    else:
        return n * countCap(n-1)

print(countCap(n))