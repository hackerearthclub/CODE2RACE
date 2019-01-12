def gcd(a, b):
    # Euclid's algorithm
    if a == 0:
        return b
    else:
        return gcd(b % a, a)


def lcm(a, b):
    return (a * b) // gcd(a, b)


print("Enter elements: ")
elements = list(map(int, input().split()))

g, l = 0, 1
for e in elements:
    g = gcd(g, e)
    l = lcm(l, e)

print("GCD = ", g)
print("LCM = ", l)