# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:00:25 2019

@author: Lee
"""

def solution(A):
    A.reverse()
    count = 0
    ans = 0
    for x in range(len(A)):
        if A[x] == 1:
            count += 1
        if A[x] == 0:
            ans += count
        if ans > 1000000000:
            return -1
    return ans

A = [1,0,1,0,1]
solution(A)