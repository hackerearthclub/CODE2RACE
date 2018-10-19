"""Empty Bottles ,
Solved by - Paritosh Mahajan , github - paritoshM9
"""

t = int(input())

for t_itr in range(t):
    n = int(input())

    #bottles_height = []
    total_height = 0
    bottles_height = (input().strip().split(' '))
    for i in range(n):

        bottles_height[i] = int(bottles_height[i])
        total_height += bottles_height[i]

    bottles_full = int(total_height/100)
    print(bottles_full)

