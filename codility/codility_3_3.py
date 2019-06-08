# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 06:50:01 2019

@author: Lee
"""

A = [3,1,2,4,3]
def solution(A):
    left = sum(A)
    right = 0
    min = 100000000
    for i in reversed(A[1:]):
        left -= i
        right += i
        diff = left - right

        if diff < 0:
            diff = -diff

        if min > diff:
            min = diff

    return min