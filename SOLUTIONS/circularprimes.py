n = int(input())

def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            sieve[i+val::val] = [0]*tmp
    return sieve

arr = ([2] + [i*2+1 for i, v in enumerate(sieve_for_primes_to(n+1)) if v and i>0])

def reversed_n(num):
    v = str(num)
    ans = ""
    for x in range(len(v)):
        ans += v[-1]
        # print(v[-1:])
        v = v[:-1]
    return ans

ansarr = []
for v in arr:
    if v <= 11:
        ansarr.append(v)
    else:
        try:
            reversed = int(reversed_n(v))
            if arr.index(reversed) and ansarr.count(v) == 0:
                ansarr.append(v)
                ansarr.append(reversed)
        except (ValueError, IndexError):
            continue
print(sum(ansarr))