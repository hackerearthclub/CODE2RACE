# Reverses the words in a string.

def reverseWords(inputString):
    words = inputString.split(' ')
    return ' '.join(reversed(words))

if __name__ == "__main__": 
    inputString = input("Enter a string: ")
    print (reverseWords(inputString)) 
