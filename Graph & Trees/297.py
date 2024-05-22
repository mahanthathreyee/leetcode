'''
Problem: Serialize and Deserialize Binary Tree
Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Tags: String, Tree, DFS, BFS
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = ''
        curr_lvl = [root]

        while curr_lvl:
            next_lvl = []
            for node in curr_lvl:
                if node:
                    next_lvl.append(node.left)
                    next_lvl.append(node.right)
                    res += str(node.val)
                else:
                    res += '#'
                res += ','

            curr_lvl = next_lvl

        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        data = data.split(',')
        if data[0] == '#':
            return

        root = TreeNode(data[0])
        curr_lvl = [root]
        curr_idx = 0

        while curr_lvl:
            next_lvl = []
            for node in curr_lvl:
                if data[curr_idx + 1] != '#':
                    node.left = TreeNode(data[curr_idx + 1])
                    next_lvl.append(node.left)
                if data[curr_idx + 2] != '#':
                    node.right = TreeNode(data[curr_idx + 2])
                    next_lvl.append(node.right)

                curr_lvl = next_lvl
                curr_idx += 2

        return root
