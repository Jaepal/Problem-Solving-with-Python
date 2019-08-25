'''
Leetcode 162. Find Peak Element

A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.
'''

def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 2:
        return 0
    for i in range(len(nums)-1):
        if i +1 == len(nums) - 1:
            return i + 1
        if nums[i+1] < nums[i]:
            return nums.index(nums[i])