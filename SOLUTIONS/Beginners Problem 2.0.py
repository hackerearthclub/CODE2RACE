def find_best_numbers(alist):
    ''' (list) -> int
    Returns the number of even numbers in a given list.
    '''
    a=0
    for x in alist:
        if x%2==0:
            a+=1
    return a

t = int(input("Please enter the number of test cases "))
l = []
for x in range(t):
    b = input("Enter a list of numbers ").strip().split()
    for x in range(len(b)):
        b[x]=int(b[x])
    l.append(b)
for x in range(t):
    print(find_best_numbers(l[x]))


