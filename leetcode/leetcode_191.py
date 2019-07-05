'''
LeetCode 191. Number of 1 Bits

Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).
'''

def hammingWeight(n):
    return bin(n).count('1')
