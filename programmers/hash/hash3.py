"""
해시 3 - 위장
"""

def solution(clothes):
    d = {}
    answer = 1
    
    for c in clothes:
        d[c[1]] = d.get(c[1], 0) + 1
    for value in d.values():
        answer *= (value + 1)
    return answer - 1