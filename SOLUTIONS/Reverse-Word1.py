#Takes string from user and reverses it.

def reverseString(s):
    wordList = s.split(' ')
    wordList.reverse()
    rString = ''
    for i in wordList:
        rString = rString + ' ' + i
    return rString.lstrip(' ')

originalString = input("Please enter a string: ")
print(reverseString(originalString))
