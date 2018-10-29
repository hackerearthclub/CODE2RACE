def sum_square_diff(N):
  sum1 = 0
  sum2 = 0
  for num in range(1, N+1):
    sum1 += num ** 2

  for num in range(1, N+1):
    sum2 += num

  sum2 = sum2 ** 2
  return abs(sum1-sum2)

N_list = []
T = int(input())

for _ in range(T):
  N = int(input())
  N_list.append(N)
  
for N in N_list:
  print(sum_square_diff(N), end="\n") 
