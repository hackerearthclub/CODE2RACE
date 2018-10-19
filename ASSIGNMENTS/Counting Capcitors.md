An electric circuit uses exclusively identical capacitors of the same value <b>C</b>.

The capacitors can be connected in series or in parallel to form sub-units, which can then be connected in series or in parallel with other capacitors or other sub-units to form larger sub-units, and so on up to a final circuit.

Using this simple procedure and up to <b>n</b>  identical capacitors, we can make circuits having a range of different total capacitances. For example, using up to  <b>n=3</b> capacitors of  <b>60 uF</b> each, we can obtain the following <b>7</b> distinct total capacitance values:

![image](https://user-images.githubusercontent.com/28304175/47214764-94e2bd00-d3bc-11e8-908b-f91a7da86d09.png)

If we denote by  <b>D(n)</b> the number of distinct total capacitance values we can obtain when using up to  <b>n</b> equal-valued capacitors and the simple procedure described above, we have: <b>D(1)=1, D(2)=3, D(3)=7,....</b> 

Find <b>D(n)</b>.

##### Reminder : When connecting capacitors C1, C2 etc in parallel, the total capacitance is,
![image](https://user-images.githubusercontent.com/28304175/47214475-ac6d7600-d3bb-11e8-862f-28943e30c99d.png)

##### whereas when connecting them in series, the overall capacitance is given by: 
![image](https://user-images.githubusercontent.com/28304175/47214934-19354000-d3bd-11e8-989a-b7a5f53b4ed9.png)

#### Input Format

Each test file contains a single integer <b>n</b> .

#### Output Format

Output a single number i.e. <b>D(n)</b>.

#### CONSTRAINTS

1≤ n ≤ 18

#### Sample Input 
```
3
```

#### Sample Output 
```
7
```
