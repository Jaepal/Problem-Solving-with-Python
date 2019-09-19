'''
LeetCode 326. Power of Three

Given an integer, write a function to determine if it is a power of three.
'''

def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False
    while(True):
        if n == 1:
            return True
        if n % 3:
            break
        else:
            n = n // 3
    return False