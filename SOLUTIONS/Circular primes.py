primes = []
a=int(input())
for possiblePrime in range(2,a): 
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break
      
    if isPrime:
        primes.append(possiblePrime)
j=0
counter=0
l=[]
while(j<len(primes)):
  b=primes[j]
  if b not in l:
    c=str(b)
    i=0
    var=0
    st=""
    while(i<len(c)):
      if int(c) in primes:
        st+=c+" "
        c=c[1:]+c[:1]
        var=1
      else:
        var=0
        st=" "
        break
      i+=1
    if var==1:
      st=st.strip()
      cd=list(set((map(int,st.split()))))
      for i in cd:
        l.append(i)
      counter+=sum(cd)
  j+=1
print(counter)   
