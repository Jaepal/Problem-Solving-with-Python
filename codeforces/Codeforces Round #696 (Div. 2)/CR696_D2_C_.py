# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 00:56:41 2021

@author: Lee
"""

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a_set = list(set(a))
    x_list = []
    
    for i in range(len(a_set)-2, -1, -1):
        x_list.append(a_set[i] + a_set[-1])
    
    i = 0
    check = 0
    check_list = []
    check_x = 0
    x = 25
    for x in x_list:
        b = a[:]
        y = int(x)
        check_list = []
        print('x : ', x)
        while True:
            if len(b) == 0:
                check = 1
                x_check = y
                break
            big = b[-1]
            b.pop()
            if x - big in b:
                check_list.append([big, x-big])
                b.remove(x-big)
                x = big
            else:
                break
        if check == 1:
            break
        i += 1
    
    if check == 1:
        print('YES')
        print(x_list[i])
        for e in check_list:
            for ee in e:
                print(ee, end=' ')
            print()
    else:
        print('NO')