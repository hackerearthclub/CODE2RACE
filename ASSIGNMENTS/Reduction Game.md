You are playing a game called the Reduction Game. This game is played on an array a with n integers. You also have another integer k with you. The following operation will be made repeatedly on this array:

Choose any two elements ai,aj such that i?j, and min(ai,aj)>k. Decrease both ai and aj by one.
This operation should be applied to the array if it's possible to apply it. But if there are multiple valid choices of ai and aj, you can choose which ones to do first and so on. The aim is to apply the operations in such a way, so as to maximize the sum of the elements in the array at the end. Your task is to find the maximum possible sum of the final array.

<b>Input</b>
The first line of the input contains an integer T denoting the number of test cases. The description of the test cases follows.
The first line of each test case contains two integers n,k denoting the number of elements in the array a.
The second line contains n space-separated integers denoting the array a.
<b>Output:</b>
For each test case, output an integer corresponding to the maximum possible sum of the remaining array in a new line.

<b>Constraints</b>
1=T=5000
1=n=50
1=ai,k=50000<br>
<b>Sample Input:</b>
3
2 1
1 2
2 1
2 2
3 1
2 3 2<br>
<b>Sample Output:</b>
3
2
5<br>
<b>Explanation</b><br>
Example 1: The initial array is [1, 2]. In this case, there are no two elements > 1. So, no operations can be made, and this is the only final array possible. And the sum of this is 3, and hence that is the answer.

Example 2: The initial array is [2, 2]. You can decrease 1 from both the elements and get the array to [1, 1]. This is the only valid pair available, so you are forced to reduce this pair. After doing so, you can't make any more operations. So, [1, 1] is the only final array achievable, and it's sum is is 2.

Example 3: The initial array is [2, 3, 2]. You could pick the first two elements and reduce them, to get the array [1, 2, 2]. Now, you have to choose the last two elements and reduce them, to get [1, 1, 1]. This is one possible final array, whose sum is 3.

Instead, you could initially have chosen the first and third element and reduced them to get [1, 3, 1]. After this, there is no operation possible, and so this is another final array achievable. Its sum is 5, and there is nothing better than this. Hence the answer is 5.
