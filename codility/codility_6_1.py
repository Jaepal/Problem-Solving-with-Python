# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 08:08:22 2019

@author: Lee
"""

def solution(A):
    dic = {}
    for x in range(len(A)):
        dic[A[x]] = A[x]
    return len(dic)
A = [2,1,1,2,3,1]
