# arr, m = list(map(int, input().strip().split())), 0
import random
randArr = []

def randomArray(n):
    for v in range(n):
        randArr.append(random.randrange(100, 1000))
    return randArr


from time import time

t1 = time()
# arr = [1, 21, 31, 25, 68, 98, 56]
arr = randomArray(1000)
m = 0
for v in range(3):
    m = max(arr)
    arr.remove(m)
t2 = time()
print(m)
print("It took ", t2 - t1, " time to finish this algorithm.")
