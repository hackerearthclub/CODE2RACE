user_input = int(input())


def calculate_n(x):       # I still think its the faster to compute sieve for a one digit higher then to do it other way
    return int("1"+("0"* len(str(x))))


n = calculate_n(user_input)


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
# This array is now a sieve of primes up to the len(user_input) + one more digit case 400 its 1000

ansarr = []
for v in arr:
    if v > user_input:          # We are looping up to the user_input limit higher values in arr allow us to check whether
                                # they are prime num by just checking the array instead of expensive computation
        break
    if v <= 11:
        ansarr.append(v)
    else:
        try:
            reversed = int(str(v)[::-1])           # we calculate reversed number by doing string slice
            if arr.index(reversed) and ansarr.count(v) == 0:    # we check for the reversed num being part of prime nums
                ansarr.append(v)                                # then we append v
                if ansarr.count(reversed) == 0:                 # if reversed is not already appended we append
                    ansarr.append(reversed)
        except (ValueError, IndexError):                        # in case of reversed not being a prime num we get
                                                                # ValueError from search operation so we just catch
                                                                # and continue
            continue
# print(ansarr)                 # Added for debugging manually if needed
print(sum(ansarr))          # we just sum appended nums and print the sum