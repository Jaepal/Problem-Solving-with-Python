# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:41:06 2019

@author: Lee
"""
def longestCommonPrefix(strs):
    sz, ret = zip(*strs), ''
    # looping corrected based on @StefanPochmann's comment below
    for c in sz:
        if len(set(c)) > 1: break
        ret += c[0]
    return ret
