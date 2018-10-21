#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    input = raw_input  # Python 2
except:
    pass               # Python 2

if __name__ == "__main__":
    a = input("Enter a string : ")
    res = 1
    for i in range(len(a)):
        res = res * ord(a[i])
    print('ASCII value : {}'.format(res))
