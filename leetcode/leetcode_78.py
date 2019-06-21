'''
LeetCode 78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
'''


import copy

def subsets(nums):
    ans = []
    if len(ans) == 0:
            ans = [[nums[0]], []]
    for i in nums[1:]:
        tmp = copy.deepcopy(ans)
        for j in range(len(ans)):
            ans[j].append(i)
        ans.extend(tmp)
    return ans