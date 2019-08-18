'''
LeetCode 283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
'''

def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    count=nums.count(0)
    nums[:]=[i for i in nums if i != 0]
    nums+=[0]*count