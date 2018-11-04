from __future__ import print_function
# author: Harshil
string = raw_input()
product = 1

for e in string:
    product *= ord(e)

print(product)
