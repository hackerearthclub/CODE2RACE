from __future__ import print_function
if __name__ == '__main__':
    n = int(input())
    res = 0
    for number in range(0, 10 ** (n + 1)):
        sum_of_digits = sum(int(digit) ** n for digit in str(number))
        if sum_of_digits == number:
            res += sum_of_digits
    print(res)
