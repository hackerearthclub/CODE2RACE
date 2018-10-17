s = input()
ans = ''
for i in range(len(s)):
    j = i+1
    d =  set([s[i]])
    small_ans = s[i]
    while(j<len(s) and s[j] not in d):
        d.add(s[j])
        small_ans += s[j]
        j += 1
    if(len(small_ans)>len(ans)):
        ans = small_ans
print(ans)
