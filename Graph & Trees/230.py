'''
Problem: Kth Smallest Element in a BST
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Tags: Tree, BST, DFS
'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [k, -1]

        def dfs(node):
            if res[0] <= 0:
                return

            if node.left:
                dfs(node.left)

            res[0] -= 1
            if res[0] == 0:
                res[1] = node.val

            if node.right:
                dfs(node.right)

        dfs(root)
        return res[1]
