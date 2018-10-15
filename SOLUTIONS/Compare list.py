def compare(s, t):
    t = list(t)
    try:
        for elem in s:
            t.remove(elem)
    except ValueError:
        return False
    return (not t)

a = [1,2,5,4,8,6];
b = [6,8,4,6,5,2,1];

if compare(a,b)==True:
    print("Equal")
else:
    print("Not Equal")
