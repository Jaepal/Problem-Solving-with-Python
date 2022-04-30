import sys
import math

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    
    n, k = input().split()
    n = int(n); k = int(k)
    p = list(map(int, input().split()))
    ans = 0
    
    dp = [p[0]] + [0]*(len(p)-1)
    for i in range(1, len(p)):
        dp[i] = dp[i-1] + p[i]
    
    for i in range(1, n):
        if p[i] * 100 / (dp[i-1] + ans) > k:
            ans += math.ceil((p[i] * 100 / k) - dp[i-1]-ans)
            
    print(ans)