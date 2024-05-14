'''
Problem: Clone Graph
Link: https://leetcode.com/problems/clone-graph/
Tags: DFS, Graph, Hashtable
'''

from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        mem = {}
        def dfs(root):
            if not root:
                return Node()
            
            if root.val in mem:
                return mem[root.val]
            head = Node(root.val)
            mem[root.val] = head
            
            head.neighbors = [dfs(neighbor) for neighbor in root.neighbors]
            return head
        
        dfs(node)
        return mem[node.val]    
