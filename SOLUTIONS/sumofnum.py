
with open('regex_sum_107892.txt') as f:
    fdata=f.read()
import re
reObj=re.compile('\d+')
mo=reObj.findall(fdata)
n=[]
for i in mo:n.append(int(i))
print(sum(n))
