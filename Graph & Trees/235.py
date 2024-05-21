'''
Problem: Lowest Common Ancestor of a Binary Search Tree
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/ # noqa: E501
Tags: BST, DFS, Tree
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode',
                             p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p, q = sorted([p.val, q.val])

        while not (p <= root.val and root.val <= q):
            root = root.left if p <= root.val else root.right

        return root
