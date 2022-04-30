import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
a_set = list(set(a))

ans = []

for num in a_set:
    max_area = 0
    tmp_area = 0
    cont = False
    for idx, h in enumerate(a):
        if h >= num:
            tmp_area += num
        if h < num or idx == len(a)-1:
            max_area = max(max_area, tmp_area)
            tmp_area = 0
    ans.append(max_area)
print(max(ans))