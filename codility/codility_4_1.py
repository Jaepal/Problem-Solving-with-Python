# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 07:25:12 2019

@author: Lee
"""
A=[2,3,4,5,6,7]
def solution(A):
    a = sorted(A)
    num = 0
    if len(A) == 1:
        return 0
    for x in range(a[0], a[0]+len(A)):
        num += x
    if sum(A) == num:
        return 1
    else:
        return 0
    
solution(A)