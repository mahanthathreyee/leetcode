'''
Problem: LRU Cache
Link: https://leetcode.com/problems/lru-cache/
Tags: Hashmap, LikedList, Doubly Linked List, LRU Cache
'''


class Node:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.size = capacity
        self.m = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.m:
            return -1

        self.put(key, self.m[key].val)
        return self.head.next.val

    def put(self, key, value):
        if key in self.m:
            c = self.m[key]
            self._deleteNode(c)
        elif len(self.m) == self.size:
            prev = self.tail.prev
            self._deleteNode(prev)
            del self.m[prev.key]

        node = Node(key, value)
        self._addNode(node)
        self.m[key] = self.head.next

    def _deleteNode(self, p):
        p.prev.next = p.next
        p.next.prev = p.prev

    def _addNode(self, newnode):
        temp = self.head.next
        self.head.next = newnode
        newnode.prev = self.head
        newnode.next = temp
        temp.prev = newnode
