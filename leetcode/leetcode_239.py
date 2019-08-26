'''
LeetCode 239. Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position. Return the max sliding window.
'''

def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    ans = []
    if k == 0:
        return ans
    for i in range(len(nums)-k+1):
        ans.append(max(nums[i:i+k]))
    return ans