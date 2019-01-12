fname = input("Enter file name: ")
fh = open(fname)
lst=list()
for imp in fh:
 im=imp.rstrip().split()
 for word in im:
     if word in lst : continue
     else :
         lst.append(word)
 lst.sort()

 print(lst)
