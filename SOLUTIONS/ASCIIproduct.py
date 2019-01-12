# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 00:52:28 2018

@author: Ishita
"""

S = input()
product = 1
for char in S:
    product *= ord(char)
    
print(product)