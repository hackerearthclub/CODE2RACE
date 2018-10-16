import functools

def find_gcd(x, y):   
    while(y): 
        x, y = y, x % y 
    return x 

def GCD_List(arr):
	gcd = functools.reduce(find_gcd, arr)
	return(gcd)   

def find_lcm(a,b):
    return a*b // find_gcd(a,b)

def LCM_List(arr):
	LCM = functools.reduce(lambda x, y: find_lcm(x, y), arr)
	return(LCM)

a=[int(x) for x in input().split(" ")]
print("GCD of list is " + str(GCD_List(a)))       
print("LCM of List is " + str(LCM_List(a)))
