#!/bin/python3

"""
file: newYearChaos.py
author: Jay Welborn www.github.com/jaywelborn

This is a solution to the New Year Chaos problem on hackerrank.
Problem: https://www.hackerrank.com/challenges/new-year-chaos/problem
Description:
It's New Year's Day and everyone's in line for the Wonderland rollercoaster
ride! There are a number of people queued up, and each person wears a sticker
indicating their initial position in the queue. Initial positions increment by
 from  at the front of the line to  at the back.

Any person in the queue can bribe the person directly in front of them to swap
positions. If two people swap positions, they still wear the same sticker
denoting their original places in line. One person can bribe at most two
others. For example, if and  bribes , the queue will look like this: .

Fascinated by this chaotic queue, you decide you must know the minimum number
of bribes that took place to get the queue into its current state!

Function Description:
Complete the function minimumBribes in the editor below. It must print an
integer representing the minimum number of bribes necessary, or Too chaotic if
the line configuration is not possible.

minimumBribes has the following parameter(s):

q: an array of integers

Input Format:
The first line contains an integer , the number of test cases.
Each of the next  pairs of lines are as follows:
- The first line contains an integer , the number of people in the queue
- The second line has  space-separated integers describing the final state of
  the queue.

Output Format:
Print an integer denoting the minimum number of bribes needed to get the queue
into its final state. Print Too chaotic if the state is invalid, i.e. it
requires a person to have bribed more than  people.
"""


# Complete the minimumBribes function below.
def minimumBribes(q):
    total_bribes = 0
    swaps = 1
    # If any person is more than 3 places ahead of where they should be,
    # too many bribes have taken place.
    for index, item in enumerate(q):
        if item > index + 3:
            print("Too chaotic")
            return

    # Finally! A use for bubblesort!
    while (swaps != 0):
        swaps = 0
        for i in range(len(q) - 1):
            if q[i] > q[i + 1]:
                swaps += 1
                q[i], q[i + 1] = q[i + 1], q[i]
                total_bribes += 1
    print(total_bribes)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
