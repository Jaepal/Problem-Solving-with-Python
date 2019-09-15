'''
LeetCode 328. Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None
        if head.next is None: return head
        o = head
        p = o.next
        ehead = p
        while p.next is not None:
            #t = o.next
            o.next = p.next
            p.next = p.next.next
            #o.next.next = t
            o = o.next
            p = p.next
            if p is None: break
            #if o is None: break
        o.next = ehead
        return head