# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 21:09:59 2019

@author: Lee
"""

A = [9,7,9,5,3,7,3]
A[2]

def solution(A):
    length = len(A)
    if length == 1:
        return A[0]
    
    a=sorted(A)
    flag, count = 0, 1
    
    for x in range(1, length):
        if a[flag]==a[x]:
            count += 1
        else:
            if count%2==0:
                flag, count = x, 1
                if x==length-1:
                    return a[x]
            else:
                return a[flag]

solution(A)