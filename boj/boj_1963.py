import sys

input = sys.stdin.readline



def search(start, target):
    v = [start]
    a_fp = [0] * (N+1)
    while v:
        num = v.pop(0)
        print(num)
        for j in range(4):
            for k in range(10):
                tmp = str(num)[:j] + str(k) + str(num)[j+1:]
                tmp = int(tmp)
                if a[tmp] == True and a_fp[tmp] == 0:
                    if tmp == target:
                        a_fp[target] = a_fp[num] + 1
                        #return a_fp[target]
                    else:
                        a_fp[tmp] += 1
                        v.append(tmp)
        
#start, target = int(p1), int(p2)
N = 10000
a = [False, False] + [True] * (N-1)
for i in range(2,N+1):
    if a[i]:
        for j in range(2*i, N+1, i):
            a[j] = False

T = int(input())
for i in range(T):
    p1, p2 = input().split()
    search(int(p1), int(p2))