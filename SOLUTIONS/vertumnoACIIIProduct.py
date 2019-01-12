# Author: Lucas Gomes Dantas - vertumno

n = input("Type in the string to know the ACIII Product: ")
product = 1
for char in n:
  product = product * ord(char)
print(product)
