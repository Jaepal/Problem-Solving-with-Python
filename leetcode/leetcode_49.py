'''
LeetCode 49. Group Anagrams

Given an array of strings, group anagrams together.
'''

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    str_set = []
    tmp = []
    ans = []
    for word in strs:
        for s in word:
            tmp.append(s)
        tmp = sorted(tmp)
        if tmp not in str_set:
            str_set.append(tmp)
            ans.append([word])
        else:
            ans[str_set.index(tmp)].append(word)
        tmp = []
    return ans

def groupAnagrams2(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    d = {}
    for w in strs:
        key = tuple(sorted(w))
        d[key] = d.get(key, []) + [w]
    return list(d.values())

