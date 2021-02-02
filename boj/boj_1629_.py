import sys; input = sys.stdin.readline

a, b, c = map(int, input().split())

n = 1
c_list = []
mod_list = []

while n*2 < c:
    n *= 2

idx = c
ans = 1
while n != 0:
    if idx >= n:
        idx -= n
        ans *= a ** n % c
    n //= 2

print(ans % c)