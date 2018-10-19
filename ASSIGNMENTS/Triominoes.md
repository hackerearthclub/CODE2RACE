A triomino is a shape consisting of three squares joined via the edges. There are two basic forms:

![image](https://user-images.githubusercontent.com/28304175/47215436-0ae82380-d3bf-11e8-9945-38c2fc41879a.png)

If all possible orientations are taken into account there are six:

![image](https://user-images.githubusercontent.com/28304175/47215451-1cc9c680-d3bf-11e8-9540-f22fa3f3b4cc.png)

Any <b><i>n</i></b> by <b><i>m</i></b> grid for which <b><i>n</i> x <i>m</i></b> is divisible by <b>3</b> can be tiled with triominoes.

If we consider tilings that can be obtained by reflection or rotation from another tiling as different there are <b>41</b> ways a <b>2</b> by <b>9</b> grid can be tiled with triominoes:

![p_161_k9](https://user-images.githubusercontent.com/28304175/47215712-0e2fdf00-d3c0-11e8-804c-6b49947cc4dc.gif)

In how many ways can a  <b><i>n</i></b> by <b><i>m</i></b> grid be tiled in this way by triominoes? 
Print answer modulo ((10^9) + 7).


#### Input Format

First line contains <b><i>n</i></b> and <b><i>m</i></b>.


#### Output Format

Print one integer i.e. answer modulo <b>1000000007 = (10^9) + 7</b>

#### CONSTRAINTS
1≤ n ≤ 6

1≤ m ≤ 21

<b><i>n</i> x <i>m</i></b> is divisible by <b>3</b>

#### Sample Input 
```
2 9
```

#### Sample Output 
```
41
```
