# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 05:17:05 2019

@author: Lee
"""

nums1 = [1,5]
nums2 = [2,4]

def solution(nums1, nums2):
    nums = nums1 + nums2
    nums = sorted(nums)
    length = len(nums)
    if length % 2 == 0:
        ans = (nums[length//2 -1] + nums[length//2])/2
    else:
        ans = nums[length//2]
    
    return ans

solution(nums1, nums2)