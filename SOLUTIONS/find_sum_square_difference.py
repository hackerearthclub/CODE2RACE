# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

message = "Pick a number:"
a = input(message)
a = int(a)

if a > 10**4:
    print("Number needs to be less than 10,000")

if a <= 10**4:
    
    #computing the sum of the squares
    somma_square = 0
    for i in range(1,a+1):
        square1 = i**2
        somma_square1 = somma_square + square1
        somma_square = somma_square1
    
    #computing the square of the sum
    somma = 0
    for i in range(1,a+1):
        somma1 = somma + i
        somma = somma1
        square_somma = somma**2
    
    #taking the absolute value of the difference
    diff = abs(somma_square - square_somma)
    print(diff)
    
