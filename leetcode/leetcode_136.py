'''
LeetCode 136. Single Number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
'''

def singleNumber(nums):
    ans = []
    for i in nums:
        if i not in ans:
            ans.append(i)
        else:
            ans.remove(i)
    return ans.pop()
