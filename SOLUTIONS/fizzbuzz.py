import sys
input()
tests = input().split()
output = []

for test in tests:
    for n in range(1, int(test) + 1):
        if n % 15 == 0:
            output.append("FizzBuzz")
        elif n % 3 == 0:
            output.append("Fizz")
        elif n % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(n))

print("\n".join(output), file=sys.stdout)
