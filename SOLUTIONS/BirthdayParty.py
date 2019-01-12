# -*- coding: utf-8 -*-

T = int(input())
for index in range(T):
    N, Q = list(map(int, input().split()))
    arr = []
    for i in range(N):
        temp = list(map(int, input().split()))
        arr.append(temp)
        
    for i in range(Q):
        t = int(input())
        count = 0
        for j in range(N):
            if arr[j][0] <= t:
                if arr[j][1] >= t:
                    count += 1
        print(count)