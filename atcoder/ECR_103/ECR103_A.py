'''
알아볼것
n, k 처리

'''

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = input().split()
    n = int(n); k = int(k)
    if n < k:
        if k % n == 0:
            print(k // n)
        else:
            print(k // n + 1)
    elif n == k:
        print(1)
    elif n > k:
        if n % k == 0:
            print(1)
        else:
            print(2)