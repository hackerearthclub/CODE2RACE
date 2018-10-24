import os
import sys

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(input().rstrip().split())
    r = d % n
    i = 0
    if d==n/2:
        for i in range(d):
            a[i],a[i+d]=a[i+d],a[i]
    else:
        t = a[0]
        while(i%n!=(n-r)):
            a[i%n] = a[(i+r)%n]  
            i = i+r
        a[n-r] = t
    
    print(" ".join(a))
            
