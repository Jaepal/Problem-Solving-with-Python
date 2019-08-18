"""
LeetCode118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 0:
        return []
    row = [1]
    ans = [[1]]
    for i in range(numRows-1):
        tmp = [0] + row
        row = row + [0]
        row = [sum(l) for l in zip(tmp, row)]
        ans.append(row)
    return ans