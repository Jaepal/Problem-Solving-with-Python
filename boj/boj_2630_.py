import sys

input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

white = 0
blue = 0

def cut(x, y, n):
    global blue, white
    check = matrix[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != matrix[i][j]:
                cut(x, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y, n//2)
                cut(x+n//2, y+n//2, n//2)
                return
    
    if check == 0:
        white += 1
        return
    else:
        blue += 1
        return

cut(0, 0, N)
print(white)
print(blue)