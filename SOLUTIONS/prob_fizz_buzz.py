
def main():
    t = -1
    acceptable = False
    while not 1 <= t <= 10:
        t = int(input("Please give the T:"))

    while not acceptable:
        n = input("Please give the N:")
        numbers = n.split()

        if len(numbers) != t:
            print("Given numbers length does not match T value\nPlease make sure there is a blank between every number")
        else:
            acceptable = True
            numbers = list(map(int, numbers))

    for i in range(1,max(numbers) + 1):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 5 == 0 :
            print('Fizz')
        elif i % 3 == 0:
            print('Buzz')
        else:
            print(i)

if __name__ == '__main__':
    main()
