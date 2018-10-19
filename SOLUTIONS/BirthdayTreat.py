# -*- coding: utf-8 -*-

T = int(input())
for index in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    total_gifts = sum(C)
    if total_gifts % len(C) == 0:
        gifts_avg = total_gifts // len(C)
        min_moves = 0
        for i in range(N):
            if C[i] > gifts_avg:
                diff = C[i] - gifts_avg
                min_moves += diff
        print(min_moves)
    else:
        print("No Treat")