'''
268. Missing Number

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
    while(True):
        ans = l.pop()
        if ans != nums.pop(0):
            break
    return ans