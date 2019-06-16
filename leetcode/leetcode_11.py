'''
Leetcode 11. Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
'''


def maxArea(height):
    res, l, r = 0, 0, len(height) - 1
    while l < r:
        h = min(height[l], height[r])
        res, l, r = max(res,  h * (r - l)), l + (height[l] == h), r - (height[r] == h)
    return res


'''
핵심 아이디어:
맨 처음과 끝에서 시작해서 넓이를 구하고 양 끝 중에서 작은 쪽을 좁히는 방식으로 반복
'''