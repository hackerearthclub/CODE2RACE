# -*- coding: utf-8 -*-

T = int(input())
for index in range(T) :
    N, M, L = list(map(int, input().split()))
    arr = []
    for i in range(N) :
        B = list(map(int, input().split()))
        arr.append(B)
    
    tot_speed = 0
    time = 0
    maximum = 0
    while(maximum < M):
        for  i in range(N) :
            v = arr[i][0] + (arr[i][1] * time)
            if v >= L:
                tot_speed += v
        maximum = tot_speed
        time += 1
        
    print(time)