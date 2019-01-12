import unittest

def empty_bottles(num_bottles, bottle_heights):
    heights_arr = bottle_heights.split(' ')
    heights_arr = heights_arr[:num_bottles]
    total_height = 0
    for x in heights_arr:
        total_height = total_height + int(x)
    answer = num_bottles - round(total_height/100)
    return answer

class EmptyBottlesTestCase(unittest.TestCase):

    def test_heights_arr(self):
        num_bottles = '6'
        bottle_heights = '20 40 50 30 90 100'
        self.assertEqual(
            empty_bottles(num_bottles, bottle_heights),
            3
        )


if __name__ == '__main__':
    test_case = input()
    test_case = int(test_case)

    while test_case > 0:
        num_bottles = input()
        num_bottles = int(num_bottles)
        bottle_heights = input()
        print('Answer: ', empty_bottles(num_bottles, bottle_heights))
        test_case = test_case - 1
    # uncomment bottom line to test
    # unittest.main()

#for test in range(int(input())):
#    N=int(input())
#    org=list(map(int,input().split()))
#    print(sum(org)//100)
