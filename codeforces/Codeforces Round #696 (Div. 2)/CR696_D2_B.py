# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 00:33:41 2021

@author: Lee
"""

t = int(input())


n=30000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

for _ in range(t):
    d = int(input())
    i = 0
    tmp = 1
    lst = []
    while True:
        if len(lst) >=2:
            break
        if primes[i] - tmp >= d:
            lst.append(primes[i])
            tmp = primes[i]
        i += 1
    print(lst[0] * lst[1])