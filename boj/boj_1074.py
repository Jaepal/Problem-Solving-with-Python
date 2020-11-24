import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())
ans = 0
while N > 0:
    count = 0
    if r > 2**(N-1)-1:
        count += 2
        r = r - 2**(N-1)
    if c > 2**(N-1)-1:
        count += 1
        c = c - 2**(N-1)
    
    ans += 4**(N-1)*count
    N -= 1
print(ans)