#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

if __name__ == "__main__":
    a = raw_input("Enter a string : ")
    res = 1
    for i in range(len(a)):
        res = res * ord(a[i])
    print('ASCII value : {}'.format(res))
