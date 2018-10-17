# Convertion from text to ASCII codes
def ASCIISentence( str ): 
    c =1
    for i in str: 
        print(ord(i), end = '') 
        c*=ord(i)
    print('\nproduct of ascii values=\n', c) 
      
# Driver code 
str = "IS"
print("ASCII Sentence:") 
ASCIISentence(str) 