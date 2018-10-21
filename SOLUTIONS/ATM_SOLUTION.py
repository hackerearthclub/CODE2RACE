t = int(input())

for _ in range(t):
    n,total_amt = [int(v) for v in input().split()]
    peope_amt = [int(v) for v in input().split()]
    result=""
    for i in range(len(peope_amt)):
            if(total_amt>=peope_amt[i]):
                total_amt=total_amt-peope_amt[i]
                result=result+"1"
            else:
                result+="0"
                
           
print(result)
