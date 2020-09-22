'''''''''''''''
===============
  제출한 풀이
===============
'''''''''''''''

N = int(input())
arr = list(map(int, input().split()))
 
arr.sort()
 
p = int(arr[-1]**(1/(N-1)))-1
seq = 1
 
while True:
    diff = 0
    for i in range(N):
        diff += abs(arr[i] - p**i)
    if seq < 2:
        ans = diff
    else:
        if ans > diff:
            ans = diff
        else:
            break
    p += 1
    seq += 1
print(ans)