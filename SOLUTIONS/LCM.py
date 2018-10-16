import math

def lcm(array):
    result = array[0]
    for elem in array:
        gcd = math.gcd(result,elem)
        result = (int)(result*elem)
        result = (int)(result/gcd)
    
    return result