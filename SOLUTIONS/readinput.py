from __future__ import print_function
import sys

fileContent = open("input.txt", "r")

for line in fileContent:
	currentLine = int(line)
	newData = currentLine * 2 
	print(newData)