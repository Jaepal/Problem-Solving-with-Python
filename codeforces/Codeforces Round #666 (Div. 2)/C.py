'''''''''''''''
===============
 Tutorial 풀이
 
i) n == 1 인 경우

마지막에 자신의 크기만큼 빼줌


ii) n != 1 인 경우

우선 처음 숫자를 자신만큼 빼줌, 그리고 순서대로 -n*a_i 만큼 빼줌
-> 그러면 모든 숫자가 (n-1)의 배수로 바뀜 ( n*a - a = (n-1)*a )
따라서 마지막에 (n-1)*a_i 를 더해주면 모든 숫자가 0이 된다.
===============
'''''''''''''''

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print('1 1', -a[0], '1 1', '0', '1 1', '0', sep='\n')
    exit(0)

print(1, n)
for i in range(n):
    print(-a[i] * n, end = ' ')
    a[i] -= a[i] * n
print()

print(1, n - 1)
for i in range(n - 1):
    print(-a[i], end = ' ')
    a[i] = 0
print()

print(2, n)
for i in range(1, n):
    print(-a[i], end = ' ')
    a[i] = 0
print()