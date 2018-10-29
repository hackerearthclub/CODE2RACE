#BeginerProblem2
n = int(input())
countBest = []
for i in range(0,n):
    countBest.append(0)
    nums = int(input())
    for j in range(0,nums):
        if int(input())%2 == 0:
            countBest[i] += 1
for i in countBest:
    print (i)
