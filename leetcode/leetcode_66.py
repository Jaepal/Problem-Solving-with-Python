'''
Leetcode 66. Plus One
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
'''

def plusOne(digits):
    s = ""
    ans = []
    for i in digits:
        s = s + str(i)
    s = int(s) + 1
    for j in str(s):
        ans.append(int(j))
    return ans