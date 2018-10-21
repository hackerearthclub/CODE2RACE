s = input().strip(".").split(" ")
s.reverse()
for i in range(len(s)):
	if i != (len(s) - 1):
		print(s[i],end=" ")
	else:
		print(s[i],end=".")