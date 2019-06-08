# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:08:55 2019

@author: Lee
"""
def solution(S,P,Q):
    M = len(P)
    N = len(S)
    A = [[0, 0, 0, 0]]
    counter = [0] * 4
    result = []
    for i in S:
        if i == "A":
            counter[0] += 1
            A.append(counter[:])
        elif i == "C":
            counter[1] += 1
            A.append(counter[:])
        elif i == "G":
            counter[2] += 1
            A.append(counter[:])
        elif i == "T":
            counter[3] += 1
            A.append(counter[:])
    
    for i in range(M):
        for j in range(4):
            val = A[Q[i]+1][j] - A[P[i]][j]
            if val != 0:
                result.append(j + 1)
                break
    
    return result
S = "CAGCCTA"
P = [2,5,0,2,1]
Q = [4,5,6,3,4]

solution(S,P,Q)