from __future__ import print_function

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3


def reverse_string(string):
    return " ".join(string.split(" ")[::-1])


string = raw_input('Enter a string containing multiple words:')
print(reverse_string(string))
