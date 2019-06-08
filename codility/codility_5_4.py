# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 12:07:48 2019

@author: Lee
"""

def solution(A,B,K):
    min_value =  ((A + K -1) // K) * K
 
    if min_value > B:
      return 0
 
    return ((B - min_value) // K) + 1

solution(101, 123456789, 10000)
