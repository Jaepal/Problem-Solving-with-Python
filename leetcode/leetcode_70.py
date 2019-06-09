'''
LeetCode 70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''


def climbStairs(n):
    first = 2
    second = 3
    third = 0
    if n == 1:
        return 1
    if n == 2:
        return first
    if n == 3:
        return second
    for i in range(n-3):
        third = first + second
        first = second
        second = third
    return third

climbStairs(6)

'''
핵심 아이디어 :

1과 2로 계단을 올라가는 방법 수 -> 한 칸 아래 계단과 두 칸 아래 계단을 올라가는 방법의 수의 합과 같음 => 피보나치 수열
'''