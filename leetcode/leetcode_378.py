# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 23:34:43 2019

@author: Lee
"""
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
i = 0

def kthSmallest(self, matrix, k):
    lst = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            lst.append(matrix[i][j])
    lst.sort()
    return lst[k-1]
print(matrix[0][1])
    