# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 06:20:02 2019

@author: Lee
"""
'''

num = 0
length=len(A)
if length == 0 or length==1:
    return A
for x in range(1, len(A)+1):
    num += x - A[x-1]
num += x+1

1+2+3+4-2-3-1-5
'''

def solution(A):
    # write your code in Python 3.6
    num = 0
    length = len(A)
    if length == 0:
        return 1
    for x in range(1, length+1):
        num += x - A[x-1]
    num += x+1
    return num

solution(A)
    
