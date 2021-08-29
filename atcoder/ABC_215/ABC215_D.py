'''
주어진 시퀀스 - N개의 양의 정수로 이루어진 리스트 A
찾아라 모든 정수 k를 1과 M(포함) 사이 다음 상태를 만족하는
gcd(A_i, k) = 1 (1 <= i <= N을 만족하는 모든 정수 i)

==정리==
k 는 1보다 크고 M 포함 작음

리스트 A의 모든 숫자의 약수를 구하고 합친 리스트 생성
그리고 하나씩 소인수 알고리즘으로 제거

'''

import sys

input = sys.stdin.readline

def finding_divisor(n):
    div_list = []
    for i in range(1, n+1):
        if n % i == 0:
            div_list.append(i)
    return div_list

def is_prime(n):
    if n>1:
        for i in range(2,n):
            if (n % i)==0:
                return False
    return True


N, M = map(int, input().split())
A = list(map(int, input().split()))
num_list = list(range(1, M+1))

list(range(0, 10, 2))
divisor = []
for e in sorted(A, reverse=True):
    isP = is_prime(e)
    if e in divisor:
        continue
    elif isP:
        divisor.append(e)
    else:
        divisor.extend(finding_divisor(e))
    
divisor = sorted(list(set(divisor)))
divisor_filter = []

filter_list = []
for n in divisor:
    if n == 1:
        continue
    else:
        filter_list.extend(list(range(0, M+1, n)))
        
filter_list = list(set(filter_list))

ans = []
for n in num_list:
    if n not in filter_list:
        ans.append(n)

print(len(ans))
for i in ans:
    print(i)
