import sys
import itertools

input = sys.stdin.readline


S, K = input().split()
K = int(K)
S = list(S)
res = []

S_list = list(set(itertools.permutations(S)))
S_list.sort()

print(''.join(S_list[K-1]))