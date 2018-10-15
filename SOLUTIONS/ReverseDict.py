#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import OrderedDict


class ReverseDict(OrderedDict):
    '''
    Constructor
    '''

    def __init__(self, dictToReverse):
        super(ReverseDict, self).__init__(
            sorted(dictToReverse.items(), key=lambda t: t[0], reverse=True))


'''
Test if the class works
'''
if __name__ == "__main__":
    testDict = {'c': 3, 'a': 1, 'd': 4, 'b': 2}
    reversedDict = ReverseDict(testDict)
    print(reversedDict)
