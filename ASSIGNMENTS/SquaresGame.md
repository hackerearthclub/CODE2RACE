Fat Tony and Fit Tony are playing the square painting game. There are n squares drawn on a plane. The sides of the squares are parallel to the axes. Squares don't intersect, but some of them can be inside others. In his turn a player can choose any square and paint it's internal area black. All squares inside the painted one are also painted black. The player can't paint the squares that were already painted. The loser is the player who can't make a turn. Determine the winner of the game if both players play optimally and Fat Tony's turn is the first. Also if Fat Tony can win the game determine which square he has to paint on his first turn in order to win. If there are many squares which guarantee victory to Fat Tony choose the one with the smallest number.

Input

The first line of input contains t - the number of test cases. Each test case starts with n - the number of squares. Next n lines consist of three integers each x, y, a - the coordinates of the lowest left corner of the square and the length of it's sides. The squares in the input are numbered from 1 to n in the order they are listed.

Constraints

1 <= t <= 10

1 <= n <= 50000

The total number of squares over all test cases in one file won't exceed 250000.

x, y won't exceed 108 in absolute value.

a will be positive and less than 108.

Output

For each test case print "Fat x", where x - is the number of square which needs to be painted on the first turn in order to win (if there are many such square chose the one with the smallest number), if Fat Tony wins or "Fit" if Fit Tony wins.

Example

#### Input:

2

5

0 0 10

15 15 1

1 1 3

5 5 1

14 14 3

2

1 1 1

3 3 1


#### Output:

Fat 2

Fit
