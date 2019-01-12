arg = input()
for a in range(0, arg):
	n = input()
	sumOfEvenValues = 0
	first = 0
	second = 1
	third = 0
	while third <= n:
		third = first + second
		if third > n:
			break
		if third % 2 == 0:
			sumOfEvenValues += third
		first, second = second, third
	print(sumOfEvenValues)
