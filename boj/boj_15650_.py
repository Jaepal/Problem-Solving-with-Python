import sys; input = sys.stdin.readline

n, m = map(int, input().split())
check = [0 for _ in range(n+1)]
result = [0 for _ in range(m)]

def backtracking(index, n, m):
    if index == m:
        for i in range(m):
            print(result[i], end=' ')
        print()
        return

    for i in range(1, n+1):
        if check[i] == 1:
            continue
        result[index] = i
        for j in range(i+1):
            check[j] = 1
        backtracking(index+1, n, m)
        for j in range(1, n+1):
            check[j] = 0

backtracking(0, n, m)