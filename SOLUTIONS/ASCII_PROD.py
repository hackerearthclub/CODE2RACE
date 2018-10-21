str=input('Enter an ASCII string: ')
mul=1
for i in range(len(str)):
    mul*=ord(str[i])
print(mul)
