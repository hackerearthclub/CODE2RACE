# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:11:24 2018

@author: keovkevin
"""
##gcd of array of elements
def gcd(x, y): 
    while(y): 
        x, y = y, x % y 
    return x 
                  
l = list(map(int,input().split())) 
num1 = l[0] 
num2 = l[1] 
gcd1 = gcd(num1, num2) 
for i in range(2, len(l)): 
    gcd1 = gcd(gcd1, l[i]) 
print(gcd1) 

##lcm of array of numbers using gcd  
def find_lcm(num1, num2): 
    if(num1>num2): 
        num = num1 
        den = num2 
    else: 
        num = num2 
        den = num1 
    rem = num % den 
    while(rem != 0): 
        num = den 
        den = rem 
        rem = num % den 
    gcd = den 
    lcm = int(int(num1 * num2)/int(gcd)) 
    return lcm 
      
l = list(map(int,input().split()))
num1 = l[0] 
num2 = l[1] 
lcm = find_lcm(num1, num2) 
  
for i in range(2, len(l)): 
    lcm = find_lcm(lcm, l[i]) 
      
print(lcm) 
  