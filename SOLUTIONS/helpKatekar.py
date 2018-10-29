from collections import Counter
import pdb
def compareFreq(num1,num2,count):
    if (int(num1)>int(num2)) & (count[num1]>count[num2]):
        return 1
    elif (int(num2)>int(num1)) & (count[num2]>count[num1]):
        return 1
    elif int(num1)==int(num2):
        return 1
    else:
        return 0

N = int(input(""))
arr = list(input("").split())
allSubSeq = [arr[i:i+j] for i in range(0,N) for j in range(1,N - i+1)]
sortedSubSeq = sorted(allSubSeq,key=len,reverse=True)
for subSeq in sortedSubSeq:
    count = Counter(subSeq)
    flags = [compareFreq(subSeq[i],subSeq[j],count) for i in range(0,len(subSeq)) for j in range(i+1,len(subSeq))]
    if len(subSeq)<=1:
        print(len(subSeq))
        break        
    elif sum(flags)/len(flags)==1:
        print(len(subSeq))
        break
