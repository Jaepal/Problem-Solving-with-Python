# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 00:50:07 2019

@author: Lee
"""

def solution(X,Y,D):
    jmp=0
    if X>=Y:
        pass
    elif (X-Y)%D == 0:
        jmp = (Y-X)//D
    else:
        jmp = (Y-X)//D+1
    
    return jmp

X=15
Y=75
D=30
solution(X,Y,D)