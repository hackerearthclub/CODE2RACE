# author: Higor Santos de Brito Dantas
# platform: python 2.7
string = raw_input()
product = 1

for e in string:
    product *= ord(e)

print product
