def productAscii(str): 
    prod = 1
    for i in range(0, len(str)): 
        prod = prod * ord(str[i]) 
  
    return prod 
  
if __name__=='__main__': 
	
    str = "Sweta"
    print(productAscii(str))
