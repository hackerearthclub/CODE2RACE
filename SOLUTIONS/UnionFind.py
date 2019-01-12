from __future__ import print_function
import sys
sys.setrecursionlimit(9999999)

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    compx = find(x)
    compy = find(y)
    if compx == compy:
        return False
    parent[compx] = compy
    return True


n, m = map(int, raw_input().split())
parent = range(n+1)
for i in range(m):
    l = raw_input().split()
    if l[0] == "C":
        a = find(int(l[1]))
        b = find(int(l[2]))
        if a == b:
            print("S")
        else:
            print("N")
    else:
        union(int(l[1]), int(l[2]))
