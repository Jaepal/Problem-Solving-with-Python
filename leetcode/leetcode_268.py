'''
LeetCode 268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
'''

def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = list(range(len(nums)))
    nums.sort()
    if l == nums:
        return l[-1] + 1
    for i in range(len(l)):
        if l[i] != nums[i]:
            break
    return l[i]

def missingNumber2(nums):
    n = len(nums)
    return n * (n+1) / 2 - sum(nums)