# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 23:34:09 2019

@author: Lee
"""

def firstUniqChar(self, s):
    letters='abcdefghijklmnopqrstuvwxyz'
    index=[s.index(l) for l in letters if s.count(l) == 1]
    return min(index) if len(index) > 0 else -1