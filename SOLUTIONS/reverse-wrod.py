# reverse-word.py

def compute():
    s = input().split()
    s = s[::-1]
    print(s)
    ans = ''
    for i in s:
        ans = ans + i + ' '
    print(ans)
        

compute()
