import sys

input = sys.stdin.readline

while True:
    l = sorted(list(map(int, input().split())))
    if l[0] == 0:
        break
    if l[0]**2 + l[1]**2 == l[2]**2:
        print('right')
    else:
        print('wrong')