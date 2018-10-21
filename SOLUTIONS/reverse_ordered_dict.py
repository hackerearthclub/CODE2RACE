"""
Write a Python program to create an instance of an OrderedDict using a given dictionary.
Sort the dictionary during the creation and print the members of the dictionary in reverse order.

"""
from __future__ import print_function

from collections import OrderedDict
from operator import itemgetter


def reverse_ordered_dict(ordered_dict):
    return OrderedDict(reversed(list(ordered_dict.items())))


unordered_dict = {"a": 10, "b": 4, "c": 5, "d": 9}
ordered_dict = OrderedDict(sorted(unordered_dict.items(), key=itemgetter(1)))
print(reverse_ordered_dict(ordered_dict))
