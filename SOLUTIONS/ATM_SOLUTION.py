t = int(input())

for _ in range(t):
    n,total_amt = [int(v) for v in input().split()]
    people_amt = [int(v) for v in input().split()]
    result=""
    for i in range(len(people_amt)):
            if(total_amt>=people_amt[i]):
                total_amt=total_amt-people_amt[i]
                result=result+"1"
            else:
                result+="0"
                
           
print(result)
