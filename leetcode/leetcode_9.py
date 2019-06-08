# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 08:14:43 2019

@author: Lee
"""

def isPalindrome(x: int):
        r=0
        if x < 0:
            return False
        else:
            a = x
        while 1:
            r += a%10
            a  = a//10 
            if not a:
                break
            r = r*10
        
        if x == r:
            return True
        else:
            return False

num = 1210
isPalindrome(num)