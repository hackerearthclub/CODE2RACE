from __future__ import print_function
import math

integers = [];

while True:
    T = input("How many integers will you test? Between 1 and 100. ")
    if T.isdigit():
        T = int(T)
        if T >= 1 and T <=100:
            break
        else:
            print("Your number of integers must be between 1 and 100. Try again. ")
    else:
        print("Give me an integer, please.")

print("Please give me your integers one by one. Integers must be between 0 and 1000. ")

while True:
    N = input("Type an integer: ")
    if N.isdigit():
        N = int(N)
        if N >= 0 and N <=1000:
            integers.append(N)
        else:
            print("Your integers must be between 0 and 1000. Try again. ")
        if len(integers) == T:
            print("Thank you!")
            break
    else:
        print("This must be an integer between 0 and 1000, try again.")

def sumFactorial (num):
    result = int(num*(num+1)/2);
    return result

for num in integers:
    answer = sumFactorial(num)
    print(answer)
