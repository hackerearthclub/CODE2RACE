import math

def gcd(array):
    result = array[0]
    for element in array:
        result = math.gcd(result,element)
        
    return result