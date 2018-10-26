# author: Higor Santos de Brito Dantas

string = raw_input()
product = 1

for e in string:
    product *= ord(e)

print product