# -*- coding: utf-8 -*-

T = int(input())
for index in range(T):
    N = int(input())
    max_pp = -1
    
    for num in range(1, N+1):
        pan = False
        num_str = str(num)
        count = 0
        for i in range(1, len(num_str) + 1):
            if str(i) in num_str:
                count += 1
        if count == len(num_str):
            pan = True
            
        if pan == True:
            prime = True
            i = 1
            num_fact = 0
            while (i <= (num ** 1/2)):
                if num % i == 0:
                    num_fact += 1
                i += 1
            if num_fact != 1:
                prime = False
                
        if pan == True and prime == True:
            max_pp = num
            
    print(max_pp)