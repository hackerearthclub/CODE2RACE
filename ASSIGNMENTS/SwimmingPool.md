The summer is coming and Chef wants to fill his swimming pool with water so that he could enjoy swimming in it during these hot days.

The swimming pool is N metres in length (long course) and a fixed width 1 metre. Its long course is split into N equal parts, with possibly different depths. For each valid i, the i-th part has depth Di metres.

You should process Q queries. There are two types of queries:

1xv — pour v cubic metres of water into the x-th part of the pool
2x — find how much metres deep is the water surface from the ground in the x-th part of the pool. If there's no water on this part then the water surface depth is same as the depth of this part.
Water level obeys the following rules. As long as the water level in some part of the pool is higher than the water level in at least one of the adjacent parts, the water from it will move to adjacent parts with lower water levels until water levels become equal or there is no water left in this part. If the adjacent part from both sides (left and right) have lower water level then the half of the quantity of water in the current part will move to left and the other half will move to the right. The water on the leftmost part can't move to the left, and the water on the rightmost part can't move to the right.

When the water level reaches the surface of the pool (i.e. its depth become 0), the pool overflows and the water level does not increase anymore.

Please refer to the samples for more clarification.


Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and Q.
The second line contains N space-separated integers D1,D2,…,DN.
Q lines follow. Each of these lines describes a query in the format 1xv or 2x.

Output
For each query of the second type, print a single line containing one real number — the depth of the water surface of the x-th part of the pool if it contains water, or Dx if it does not. Your answer will be considered correct if its relative or absolute error does not exceed 10−6.

Constraints
1≤T≤100
1≤N,Q≤105
the sum of N in all test cases does not exceed 105
the sum of Q in all test cases does not exceed 105
1≤Di≤109 for each valid i
1≤v≤1014

Subtasks
Subtask #1 (30 points): there is at most one query of the first type

Subtask #2 (30 points): all queries of the first type appear before any queries of the second type

Subtask #3 (40 points): original constraints
Example Input:-
4
5 6
3 5 2 1 6
1 4 2
2 2
1 2 3
2 2
2 5
2 3
6 8
5 5 1 1 2 2
1 4 1
1 1 1
2 1
2 2
2 3
2 4
2 5
2 6
7 8
8 3 5 1 5 3 8
1 4 7
2 1
2 2
2 3
2 4
2 5
2 6
2 7
3 4
1 2 1
1 1 10
2 1
2 2
2 3

Output:
Example Output
4.0000000000
2.0000000000
5.0000000000
2.0000000000
4.2500000000
4.2500000000
1.0000000000
1.0000000000
1.7500000000
1.7500000000
6.5000000000
3.0000000000
3.0000000000
1.0000000000
3.0000000000
3.0000000000
6.5000000000
0.0000000000
0.0000000000
0.0000000000
Explanation
Example case 1: The pool is divided into 5 parts, the depths of the parts are 3 5 2 1 6, in first query we pour 2 cubic units of water into 4-th part, since both 3-th part and 5-th part are deeper than 4-th part then the water can't stay in 4-th part, 1 unit will go to left and 1 unit to right. the 1 unit that went to the right stayed in 5-th part and made its depth equal to 5, the 1 unit that went to the right couldn't stay in 3-th part because 2nd part is deeper than it so it moved to 2nd part and made its depth equal to 4.

in the third query we pour 3 water units into 2nd part, in the beginning 2nd part is deeper than than 1st part and 3rd part so water will stay in 2nd part until its depth become 3 it will have same depth as 1st part so the remaining water will be evenly distributed between 1st and 2nd parts.

Example case 2: in the first query we pour 1 cubic unit of water above 4th part, since it has same depth as 3rd part, and both 2nd and 5th parts are deeper than 4th part then 0.5 units of water will go to 5th part (and will be distributed equally between 5th and 6th parts) and 0.5 units of water will go to 2nd part (and will be ditributed equally between 1st and 2nd parts). so after first query depths of all parts will become (4.75 4.75 1.00 1.00 1.75 1.75).

Example case 4: The pool overflowed so all parts has 0 depth
