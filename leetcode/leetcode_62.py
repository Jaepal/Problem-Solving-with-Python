'''
LeetCode 62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
'''

def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    l = [1] * (m+1)
    l[0] = 0
    while(n-1):
        for i in range(1, len(l)):
            l[i] = l[i] + l[i-1]
        n -= 1
    return l[m]