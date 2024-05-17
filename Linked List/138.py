'''
Problem: Copy List with Random Pointer
Link: https://leetcode.com/problems/copy-list-with-random-pointer/
Tags: Hashmap, LikedList
'''


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):

        # Insert each node's copy right after it, already copy .label
        node = head
        while node:
            copy = Node(node.val)
            copy.next = node.next
            node.next = copy
            node = copy.next

        # Set each copy's .random
        node = head
        while node:
            node.next.random = node.random and node.random.next
            node = node.next.next

        # Separate the copied list from the original, (re)setting every .next
        node = head
        copy = head_copy = head and head.next
        while node:
            node.next = node = copy.next
            copy.next = copy = node and node.next

        return head_copy
