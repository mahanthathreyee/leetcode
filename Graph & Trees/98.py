'''
Problem: Validate Binary Search Tree
Link: https://leetcode.com/problems/validate-binary-search-tree/
Tags: Binary Search, Trees
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], low=-float('inf'), high=float('inf')) -> bool:
        if not root: 
            return True
        if root.val >= high or root.val <= low: 
            return False

        return self.isValidBST(root.left, low, root.val) \
                and self.isValidBST(root.right, root.val, high)
