for _ in range(int(input())):
    n = int(input())
    fact = 1
    if n== 0 :
        fact = 1
    else:
        for i in range(1,n + 1):
            fact = fact*i
    tot=0
    while(fact>0):
        dig=fact%10
        tot=tot+dig
        fact=fact//10 
    print(tot)     
    