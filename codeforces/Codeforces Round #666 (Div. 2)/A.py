'''''''''''''''
===============
  제출한 풀이
===============
'''''''''''''''


N = int(input())
 
for _ in range(N):
    d = {}
    ans = 0
    M = int(input())
    for _ in range(M):
        string = input()
        for s in string:
            if s not in d.keys():
                d[s] = 1
            else:
                d[s] += 1
    for v in d.values():
        if v % M != 0:
            ans += 1
    if ans != 0:
        print('NO')
    else:
        print('YES')

