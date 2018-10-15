
a = [1, 2, 3, 1, 2, 3]
b = [3, 2, 1, 3, 2, 1]

def compare(a, b):
    return sorted(a) == sorted(b)

print(compare(a,b))
