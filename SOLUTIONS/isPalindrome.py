def palindrome(word):
    return (word == word[::-1])

word = input("Enter a word ")
if(palindrome(word)):
    print(word+" is a palindrome")
else:
    print(word+" is not a palindrome")