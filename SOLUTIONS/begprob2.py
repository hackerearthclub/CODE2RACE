#Issue no: #682
#t = no. of test cases
#n = no. of elements in list
#l = list 
# intialize count = 0 for every test case 
# if elements is % 2 == 0 then increment count by print count
t = int(input())
for i in range(t):
    count = 0
    n = int(input())
    l = list(map(int,input().split()))
    for j in l:
        if j % 2 == 0:
            count+=1
    print(count) 