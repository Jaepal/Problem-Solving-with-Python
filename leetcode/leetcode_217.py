'''
LeetCode 217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''


def containsDuplicate(nums):
    if len(nums) == 0:
        return False
    lst = sorted(list(set(nums)))
    if lst == sorted(nums):
        return False
    else:
        return True
