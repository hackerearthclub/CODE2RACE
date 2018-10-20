# -*- coding: utf-8 -*-
T = int(input())
for index in range(T):
    N = int(input())
    H = list(map(int, input().split()))

    total_water = sum(H)
    num_bottles = 0
    while(total_water >=0):
        total_water -= 100
        num_bottles +=1
    print(num_bottles - 1)