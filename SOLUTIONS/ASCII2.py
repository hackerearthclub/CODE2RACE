#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = raw_input("Enter a string : ")
    res = 1
    for i in range(len(a)):
        res = res * ord(a[i])
    print('ASCII value : ',res)

