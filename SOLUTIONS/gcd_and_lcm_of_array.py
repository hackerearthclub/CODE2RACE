import sys
import numpy as np
from math import gcd as mathgcd

def numpy_set_gcd(a):
    a = np.unique(a)
    if not a.dtype == np.int or a[0] <= 0:
        raise ValueError("Enter positive value of array elements")

    gcd = a[0]
    for i in a[1:]:
        gcd = mathgcd(i, gcd)
        if gcd == 1:
            return 1 

    return gcd

a=[int(x) for x in input().split()]
b=numpy_set_gcd(a)
c=np.lcm.reduce(a)
sys.stdout.write("GCD of given array is ")
print(b)
sys.stdout.write("LCM of given array is ")
print(c)
