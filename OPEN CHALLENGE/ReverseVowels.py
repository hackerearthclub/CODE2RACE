#ReverseVowels
s = input()
dict_vow = ["a" , "e", "i", "o" , "u", "A" , "E", "I", "O" , "U"]
str_lists = list(s)
vow_lists = []
pos_lists = []
count = 0
for str_list in str_lists:
    if str_list in dict_vow:
        vow_lists.append(str_lists[count])
        pos_lists.append(count)
    count+=1
count = len(vow_lists)-1
for vow_list in vow_lists:
    str_lists.pop(pos_lists[count])
    str_lists.insert(pos_lists[count], vow_list)
    count-=1
print (''.join(str_lists))
