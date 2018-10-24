# Compare Lists

def compare_lists(listA, listB):
    out = (sorted(listA) == sorted(listB))
    return out


list_1 = [1,2,3]
list_2 = [2,4,1]

print(compare_lists(list_1, list_2))
