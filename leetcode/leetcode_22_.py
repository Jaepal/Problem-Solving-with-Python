'''
LeetCode 22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    ans = []
    def generate(S='', left = 0, right = 0):
        if len(S) == n * 2:
            ans.append(S)
            return
        if left < n:
            generate(S+'(', left+1, right)
        if right < left:
            generate(S+')', left, right+1)
    generate()
    return ans