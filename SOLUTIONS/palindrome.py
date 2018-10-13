
def isPalindrome(a):
    return str(a) == str(a)[::-1]

def largestPalindrome(inn):
    out = 0
    for i in range(990,99,-11):
        for j in range(999,99,-1):
            a = i*j
            if a>out and a < inn and isPalindrome(a):
                out=a
            elif a<out:
                break
    return out

inputStr = """2
101110
800000"""

inputList=inputStr.split("\n")[1:]

for i in inputList:
    print(largestPalindrome(int(i)))
