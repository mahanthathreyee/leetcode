'''
Problem: Add Two Numbers
Link: https://leetcode.com/problems/add-two-numbers/
Tags: LikedList, Recursion, Math
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, A: Optional[ListNode],
                      B: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        root = node = ListNode()

        while A or B:
            x = y = 0
            if A:
                x, A = A.val, A.next
            if B:
                y, B = B.val, B.next
            s = x + y + c
            c = s // 10

            node.next = ListNode(s - (c * 10))
            node = node.next

        if c:
            node.next = ListNode(c)

        return root.next
