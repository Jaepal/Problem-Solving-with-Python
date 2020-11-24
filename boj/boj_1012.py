import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline


t = int(input())


dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def dfs(y, x):
    visited[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if visited[ny][nx] == 0 and matrix[ny][nx] == 1:
                dfs(ny, nx)

for _ in range(t):
    m, n, k = map(int, input().split())
    matrix = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        matrix[b][a] = 1
    visited = [[0]*m for _ in range(n)]
    inum = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and matrix[i][j] == 1:
                dfs(i, j)
                inum += 1
    print(inum)