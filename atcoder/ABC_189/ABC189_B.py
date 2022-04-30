import sys

input = sys.stdin.readline

N, X = input().split()
X = float(X)
d = 0
lst = []
bf = 0

for i in range(int(N)):
    V, P = input().split()
    now = int(V) * int(P) / 100
    lst.append(bf + now)
    bf += now

if X >= lst[-1]:
    print(-1)
    
else:
    for n, l in enumerate(lst):
        if l > X:
            print(n+1)
            break