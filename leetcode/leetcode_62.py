# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 22:34:56 2019

@author: Lee
"""
m = 7
n = 3
i = 2
def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    l = [1] * (m+1)
    l[0] = 0
    while(n-1):
        for i in range(1, len(l)):
            l[i] = l[i] + l[i-1]
        n -= 1
    return l[m]

uniquePaths(7, 3)