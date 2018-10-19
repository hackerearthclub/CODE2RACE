# -*- coding: utf-8 -*-

N = int(input())
cp_sum = 0

for i in range(1, N+1):
    counter = 0
    for index in range(len(str(i))):
        i = str(i)
        i = i[len(i)-1] + i[:len(i)-1]
        rot_num = int(i)
        
        j = 1
        num_fact = 0
        prime = True
    
        while(j <= (rot_num ** 1/2)):
            if rot_num % j == 0:
                num_fact += 1
            j += 1
            
        if num_fact != 1:
            prime = False
        
        if prime == True:
            counter += 1
            
    if counter == len(str(i)):
        cp_sum += int(i)
        
print(cp_sum)