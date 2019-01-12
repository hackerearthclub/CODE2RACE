from __future__ import print_function
word = raw_input("Insert a long string: ").split()
output = ''

for x in xrange(len(word)-1,0,-1):
	output += word[x] + " "

output += word[0]
print(output)

