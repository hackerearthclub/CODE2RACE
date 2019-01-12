# Even Fibonacci numbers
# Mariana

def FibSeq(n):
    count = 0
    a,b = 1,2
    while a < n:
        if a%2 == 0: # because I only want even numbers
            count += a
        a, b = b , a+b
    return count

T = int(input('Enter number: '))

val_list  = input().split(",")
for i in range(T):
	print(FibSeq(int(val_list[i])))


