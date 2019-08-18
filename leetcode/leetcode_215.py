'''
LeetCode 215. Kth Largest Element in an Array

Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''
def findKthLargest(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    list_sort = sorted(nums)
    return list_sort[-k]