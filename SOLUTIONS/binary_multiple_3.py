# Binary Multiple of 3

def bin_mult_tree(number):
    numberBin = '0b'
    numberBin += number
    number = int(numberBin, 2)

    if(number%3 == 0):
        out = 1
    elif(number%3 != 0):
        out = 0
    
    return out

t = int(input())
for i in range(t):
    number = str(input())
    print(bin_mult_tree(number))

