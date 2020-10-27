n, d = map(int, input().split())
ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    dist = a**2 + b**2
    if dist < d ** 2:
        ans += 1
print(ans)