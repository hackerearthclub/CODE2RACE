def isPrime(n):
    """
    Simple primality test
    """    
    if n < 2:
        return False
    
    for k in range(2, n):
        if n % k == 0:
            return False
    return True


def findSubArray(list):
    """ 
    Finds the largest sub-array having primes strictly greater than non-primes
    i.e. 
    findSubArray([4, 7, 4, 7, 11, 5, 4, 4, 4, 5]) =
    findSubArray([1, 9, 3, 4, 5, 6, 7, 8 ]) =
    """
    # converts number list to a list of 0,1 indicated by its primality 
    binaryArray = [int(isPrime(k)) for k in list]
    
    # explore subarrays from biggest (length of list) to smallest (length=2)
    # breaks when one subarray matches the requirements 
    lengthSubArray = len(binaryArray)
    found = False
    while( lengthSubArray > 1 and not found ):
        
        # move startIndex to create subarrays from same length
        numberSubArrays = len(binaryArray) - lengthSubArray + 1
        for startIndex in range(0, numberSubArrays):
            endIndex = startIndex + lengthSubArray
            binarySubArray = binaryArray[startIndex:endIndex]
            
            # verify condition requested in subarray is met
            found = sum(binarySubArray) > (lengthSubArray / 2)
            if found: break
        
        lengthSubArray -= 1 
    
    # returns the subarray using the indexes from the binarySubArray found
    return list[startIndex:endIndex]
    

def solveProblem(list):
    """
    trivial function to return the specific length that problem asked
    """
    return len(findSubArray(list))


# Tests
arrays = [[4, 7, 4, 7, 11, 5, 4, 4, 4, 5],[1, 9, 3, 4, 5, 6, 7, 8 ]]
for array in arrays :
    subArray = findSubArray(array)
    print("The array {} has an ideal subarray {} of length {}.".format(
            array, subArray, len(subArray)))
