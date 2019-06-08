# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 06:00:22 2019

@author: Lee
"""

def solution(X, A):
    if len(A)<X:
        return -1
    B=[False] * (X+1)
    B[0] = True
    frog_position = 0
    for i in range(len(A)):
        if B[A[i]] == False:
            B[A[i]] = True
            while frog_position < X and B[frog_position + 1] == True:
                frog_position += 1
            if frog_position == X:
                return i
    
    return -1

A = [1,3,1,4,2,3,5,4]
X = 5
solution(5,A)