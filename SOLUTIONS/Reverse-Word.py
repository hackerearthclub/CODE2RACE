def reverse(string):
	stringList = string.split()
	stringList.reverse()
	newString = " ".join(str(x) for x in stringList)
	return newString

arg = raw_input()
res = reverse(arg)
print res
