# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 03:38:16 2019

@author: Lee
"""

def solution(A):
    seen = [False] * len(A)
    for value in A:
        if 0 < value <= len(A):
            seen[value-1] = True
 
    for idx in range(len(seen)):
        if seen[idx] == False:
            return idx + 1
 
    return len(A)+1
            
            
A = [0,1,2,3,5,6,7,8]
solution(A)