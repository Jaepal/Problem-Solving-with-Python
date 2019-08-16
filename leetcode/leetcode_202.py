'''
LeetCode 202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.
'''

def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    num, lst = 0, []
    while(True):
        for s in str(n):
            num += int(s) ** 2
        lst.append(num)
        n = num
        if num == 1:
            break
        if len(lst) != len(set(lst)):
            break
        num = 0

    if num == 1:
        print(True)
    else:
        print(False)

def isHappy2(n):
    mem = set()
    while n != 1:
        n = sum([int(i) ** 2 for i in str(n)])
        if n in mem:
            return False
        else:
            mem.add(n)
    else:
        return True