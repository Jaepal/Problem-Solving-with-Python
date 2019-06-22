'''
LeetCode 42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
'''


def trap(height):
    if len(height) == 0:
        return 0
    water = 0
    l1, l2 = [0] * len(height), [0] * len(height)
    start = 0
    for idx, i in enumerate(height):
        if i >= start:
            start = i
        elif i < start:
            l1[idx] = start - i

    start = 0
    
    for idx, j in enumerate(reversed(height)):
        if j >= start:
            start = j
        elif j < start:
            l2[idx] = start - j
    l2 = list(reversed(l2))
    
    for k in range(len(height)):
        water += min(l1[k], l2[k])
        
    return water
