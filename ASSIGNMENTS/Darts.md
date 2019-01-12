In the game of darts a player throws three darts at a target board which is split into twenty equal sized sections numbered one to twenty.
The score of a dart is determined by the number of the region that the dart lands in. A dart landing outside the red/green outer ring scores zero. The black and cream regions inside this ring represent single scores. However, the red/green outer ring and middle ring score double and treble scores respectively.

![image](https://user-images.githubusercontent.com/28304175/47254308-73e2a080-d47e-11e8-81e2-e5563201052c.png)

At the centre of the board are two concentric circles called the bull region, or bulls-eye. The outer bull is worth <b>25</b>  points and the inner bull is a double, worth  <b>50</b> points.

There are many variations of rules but in the most popular game the players will begin with a score <b>301</b> or <b>501</b>  and the first player to reduce their running total to zero is a winner. However, it is normal to play a "doubles out" system, which means that the player must land a double (including the double bulls-eye at the centre of the board) on their final dart to win; any other dart that would reduce their running total to one or lower means the score for that set of three darts is "bust".

When a player is able to finish on their current score it is called a "checkout" and the highest checkout is <b>170: T20 T20 D25 </b> (two treble 20s and double bull).

There are exactly 14 distinct ways to checkout on a score of <b>6</b>:

![screenshot 34](https://user-images.githubusercontent.com/28304175/47254352-fc614100-d47e-11e8-9108-4aa07163a3f0.png)

Note that <b>D1 D2</b>  is considered different to <b>D2 D1</b>  as they finish on different doubles. Moreover, the combination <b>S1 T1 D1</b>  is also considered different to  <b>T1 S1 D1</b> .

In addition we shall not include misses in considering combinations; for example,  <b>D3</b> is the same as <b>0 D3</b> and <b>0 0 D3</b> .

Now imagine you have an infinite number of darts. Now you can stop on every double you get. How many ways you have to checkout with score <b>≤ N</b> ?

 
#### Input Format

A single natural number <b> N ≤ 2^60</b> - maximum score you need to investigate.

#### Output Format

![screenshot 37](https://user-images.githubusercontent.com/28304175/47254454-8eb61480-d480-11e8-9301-f2d8694337e4.png)

#### Sample Input 
```
4
```

#### Sample Output 
```
6
```
#### Explanation
```
There are six ways: 
1) D1: score=2 
2) S1 D1: score=3 
3) D2: score=4 
4) D1 D1: score=4 
5) S2 D1: score=4 
6) S1 S1 D1: score=4
```
