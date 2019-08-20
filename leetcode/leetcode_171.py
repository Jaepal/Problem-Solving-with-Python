'''
LeetCode 171. Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.
'''

def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    ans, exp = 0, 0
    for string in s[::-1]:
        ans += (26 ** exp) * (ord(string) - 64)
        exp += 1
    return ans