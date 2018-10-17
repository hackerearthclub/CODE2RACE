#!/usr/bin/python3

from collections import defaultdict, namedtuple
import argparse

TestCase = namedtuple('TestCase', ['N', 'Q', 'guests'])

def birthday_party(T):
    times = defaultdict(int)

    for g in T.guests:
        for t in range(g[0], g[1]+1):
            times[t] += 1

    for q in T.Q:
        print(times[q])

    return times

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Help with birthday party scheduling!', formatter_class=argparse.RawDescriptionHelpFormatter, epilog='''The first input is the number of testcases.\n

The first line of each testcase contain two space separated integers N and Q, then follow N lines containing two space separated integers ai bi, the arriving and leaving time of ith friend respectively.\n

Next Q lines contains a single integer t asking the number of friends at Chef's house present at time t.''')
    parser.add_argument('-t', '--test', help='Test the program', action='store_true', dest='test')
    args = parser.parse_args()

    if args.test:
        t = TestCase(N=3, Q=[1,2,3], guests=[(1,2), (2, 2), (2, 3)])
        birthday_party(t)

    else:
        T = int(input())
        cases = []
        for _ in range(T):
            N, nQ = input().split()
            N = int(N)
            nQ = int(nQ)

            guests = []
            for _ in range(N):
                g = input().split()
                guests.append([int(g[0]), int(g[1])])
            Q = []
            for _ in range(nQ):
                Q.append(int(input()))

            cases.append(TestCase(N=N, Q=Q, guests=guests))
        for c in cases:
            birthday_party(c)



