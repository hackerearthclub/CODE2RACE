
givenString = input("Please type a string: ")
result = 1
for letter in givenString:
    result = result*ord(letter)
print(result)