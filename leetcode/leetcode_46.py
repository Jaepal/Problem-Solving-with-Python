'''
LeetCode 46. Permutations

Given a collection of distinct integers, return all possible permutations.
'''

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ans, tmp = [], []
    for n, i in enumerate(nums):
        tmp = ans
        ans = []
        for l in tmp:
            for j in range(n+1):
                l.insert(j, i)
                ans.append(l[:])
                l.remove(i)
        if not len(ans):
            ans = [[nums[0]]]
    return sorted(ans)