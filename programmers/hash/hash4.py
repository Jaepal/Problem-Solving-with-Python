"""
해시 4 - 베스트앨범
"""

def solution(genres, plays):
    d = {}
    for n, genre in enumerate(genres):
        d[genre] = d.get(genre, []) + [plays[n]]
    for l in d.values():
        l.sort(reverse=True)
    d = sorted(d.items(), reverse=True, key=lambda x: sum(x[1]))

    rank = []
    ans = []

    for i in range(len(d)):
        rank.extend(d[i][1][:2])

    for r in rank:
        ans.append(plays.index(r))
        plays[plays.index(r)] = -1
    return ans