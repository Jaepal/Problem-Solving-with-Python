import sys
import heapq

input = sys.stdin.readline

heap = []

t = int(input())

for _ in range(t):
    n = int(input())
    if n == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-n, n))
        