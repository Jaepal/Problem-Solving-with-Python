# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def num(l: ListNode):
    num = power = 0
    while l is not None:
        num += l.val * (10**power)
        power += 1
        l = l.next
    return int(num)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num_array = map(int, str(num(l1) + num(l2)))
        ln = None
        for n in num_array:
            lag = ln
            ln = ListNode(n)
            ln.next = lag
        return ln