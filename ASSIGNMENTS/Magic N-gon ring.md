Consider the following "magic" <b> 3-gon </b>ring, filled with the numbers <b>1</b> to<b> 6</b>, and each line adding to nine.

![image](https://user-images.githubusercontent.com/28304175/47213783-9e1e5a80-d3b9-11e8-8704-0cb19521fe8d.png)

Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.
#### TOTAL                  SOLUTION SET
    9                      4,2,3; 5,3,1; 6,1,2
    9                      4,3,2; 6,2,1; 5,1,3
    10                     2,3,5; 4,5,1; 6,1,3
    10                     2,5,3; 6,3,1; 4,1,5
    11                     1,4,6; 3,6,2; 5,2,4
    11                     1,6,4; 5,4,2; 3,2,6
    12                     1,5,6; 2,6,4; 3,4,5
    12                     1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the strings for a <b> 3-gon </b>ring where total is<b> 9</b> are <b>423531612</b> and <b>432621513 </b>.

Given <b> N </b>, which represents the <b> N-gon</b>  and the total<b> S</b>  print all concatenated solution strings in alphabetical sorted order.

#### Note: It is guaranteed that solution will exist for testcases.

#### Input Format

You are given <b>N</b>  and <b>S</b>  separated by a space.

#### Constraints

3 ≤ N ≤  10

#### Output Format

Print the required strings each on a new line.

#### Sample Input 
```
3 9
```

#### Sample Output 
```
423531612
432621513
```

