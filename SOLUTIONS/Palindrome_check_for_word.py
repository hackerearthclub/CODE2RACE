def palindrome_check():
    word= input("Enter a word: ")
    reverse=""
    for i in word:
        reverse= i + reverse
    if reverse== word:
        print (word,"is a palindrome")
        return True,word,"is a palindrome"
        
    else:
        print(word,"is not a palindrome")
        return False,word,"is not a palindrome"
        

palindrome_check()




    
