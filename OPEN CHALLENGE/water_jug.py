

'''
Problem Statement: Given two vessels, one of which can accommodate a liters of water and the other which can accommodate b liters of water, determine the number of steps required to obtain exactly c liters of water in one of the vessels.

At the beginning both vessels are empty. The following operations are counted as 'steps':

1. Emptying a vessel,
2. Filling a vessel,
3. Pouring water from one vessel to the other, without spilling, until one of the vessels is either full or empty.

INPUT:
T : Number of Test Cases
Each test case consists of 3 inputs
a: The number of litres 1st container can hold
b: The number of litres 2nd container can hold
c: The final amount of water one vessel should contain

CONSTRAINTS:
1<=t<=100
0<=a,b,c<=40000

OUTPUT:
For each set of input data, output the minimum number of steps required to obtain c liters, or -1 if this is impossiible.

SAMPLE INPUT:
2
5
2
3
2
3
4
SAMPLE OUTPUT:
2
-1
'''
from fractions import gcd

def problem(first_jug,second_jug,check_amount):
	first_jug_temp = first_jug
	second_jug_temp = 0
	count = 1
	while first_jug_temp!=check_amount and second_jug_temp!=check_amount:
		temp = min(first_jug_temp,second_jug-second_jug_temp)
		second_jug_temp += temp 
		first_jug_temp -= temp
		count += 1
		if first_jug_temp == check_amount or second_jug_temp == check_amount:
			break
		if first_jug_temp == 0:
			first_jug_temp = first_jug
			count += 1 
		if second_jug_temp == second_jug:
			second_jug_temp = 0
			count += 1
	return count

t = int(input())
while t>0:
	first_container_amount = int(input())
	second_container_amount = int(input())
	final_amount = int(input())
	if final_amount>max(first_container_amount,second_container_amount):
		print(-1)
	elif final_amount%gcd(first_container_amount,second_container_amount)!=0:
		print(-1)
	elif final_amount==first_container_amount or final_amount == second_container_amount:
		print(1)
	else:
		print(min(problem(first_container_amount,second_container_amount,final_amount),problem(second_container_amount,first_container_amount,final_amount)))
	t = t-1 

