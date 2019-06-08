# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 00:13:10 2019

@author: Lee
"""

def solution(A, K):
    # write your code in Python 3.6
    length=len(A)
    if length == 0 or length == 1:
        return A
    K = K%length
    
    B=[0]*length
    
    if K == 0:
        return A
    
    for x in range(length):
        if x+K<length:
            B[x+K]=A[x]
        else:
            B[x+K-length]=A[x]
    
    return B


A=[1,2,3,4,5]
K=6
solution(A, K)