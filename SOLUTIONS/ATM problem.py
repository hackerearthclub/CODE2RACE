# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 00:58:00 2018

@author: Ishita
"""

T = int(input())
for index in range(T):
    N, K = list(map(int, input().split())) 
    A = list(map(int, input().split()))
    #result = []
    result = ''
    balance = K
    for i in range(N):
        temp = balance - A[i]
        if temp >= 0:
            balance = temp
            #result.append(1)
            result += '1'
        else:
            #result.append(0)
            result += '0'
    print(result)