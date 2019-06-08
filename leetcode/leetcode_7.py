# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 07:41:47 2019

@author: Lee
"""

num = 10

def reverse(num):
    r=0
    if num < 0:
        flag = True
        a = -num
    else:
        flag = False
        a = num
    while 1:
        r += a%10
        a  = a//10 
        if not a:
            break
        r = r*10
        
    ans = r*-1 if flag else r
    
    return ans

reverse(num)