Num = int(input("Enter a number = "))

temp = Num

arm = 0
while(temp):
	arm += (temp%10)**3
	temp//=10

if(arm == Num): print(Num, "is Armstrong")
else: print(Num, "is NOT Armstrong")
