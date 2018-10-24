print("Enter the number of test cases")
t=int(input())
while(t):
    n=int(input())
    sumofsq = n*(n+1)*(2*n+1)/6
    sqofsum = ((n*(n+1))/2)**2
    print(int(abs(sumofsq-sqofsum)))
    t=t-1

