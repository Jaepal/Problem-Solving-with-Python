'''
LeetCode 3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.
'''


def lengthOfLongestSubstring(s):
    # 빈 문자열이 입력될 경우
    if len(s) == 0:
        return 0
    
    # 단일 문자열이 들어올 경우
    if len(s) == 1:
        return 1
    
    tmp = ""
    ans = ""
    
    for i in s:
        if i not in tmp:
            tmp += i
        else:
            tmp = tmp[tmp.index(i)+1:] + i
            
        if len(tmp) >= len(ans):
                ans = tmp

    return ans