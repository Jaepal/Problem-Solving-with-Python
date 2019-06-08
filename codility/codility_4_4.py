# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 05:00:18 2019

@author: Lee
"""
def solution2(N, A):
    result = [0]*N    # The list to be returned
    max_counter = 0   # The used value in previous max_counter command
    current_max = 0   # The current maximum value of any counter
    for command in A:
        if 1 <= command <= N:
            # increase(X) command
            if max_counter > result[command-1]:
                # lazy write
                result[command-1] = max_counter
            result[command-1] += 1
            if current_max < result[command-1]:
                current_max = result[command-1]
        else:
            # max_counter command
            # just record the current maximum value for later write
            max_counter = current_max
    for index in range(0,N):
        if result[index] < max_counter:
            # This element has never been used/updated after previous
            #     max_counter command
            result[index] = max_counter
    return result

def solution(N, A):
    B = [0] * N
    
    for x in range(len(A)):
        if A[x] == N + 1:
            B = [max(B)] * N
        else:
            B[A[x]-1] += 1
    return B
            
A = [3,4,4,6,1,4,4]
N = 5
solution(N,A)