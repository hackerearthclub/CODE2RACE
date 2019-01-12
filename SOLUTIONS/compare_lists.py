"""Write a Python program to compare two unordered lists (not sets)."""

from collections import Counter


def compare(list1, list2):
    return Counter(list1) == Counter(list2)


list1 = [2, 3, 4, 6, 7]
list2 = [3, 6, 7, 2, 4]
print(compare(list1, list2))
