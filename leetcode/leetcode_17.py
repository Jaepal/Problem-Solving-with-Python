'''
LeetCode 17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''



def letterCombinations(digits):
    dic = {2 : ['a', 'b', 'c'], 3 : ['d', 'e', 'f'], 4 : ['g', 'h', 'i'], 5 : ['j', 'k', 'l'], 6 : ['m', 'n', 'o'],
       7 : ['p', 'q', 'r', 's'], 8 : ['t', 'u', 'v'], 9 : ['w', 'x', 'y', 'z']}
    if len(digits) == 0:
        return []
    ans = dic[int(digits[0])]
    tmp = []
    
    for i in digits[1:]:
        tmp = []
        for j in ans:
            tmp += list(map(lambda x: str(j) + str(x), dic[int(i)]))
        ans = tmp
    return ans