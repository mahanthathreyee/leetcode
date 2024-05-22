'''
Problem: Graph Valid Tree
Link: https://leetcode.com/problems/graph-valid-tree/
Tags: BFS, DFS, Tree
'''

from collections import defaultdict


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        adj = defaultdict(list)
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visited = set()

        def dfs(root=0, prev=-1):
            if root in visited:
                return False

            visited.add(root)
            for node in adj[root]:
                if node == prev:
                    continue
                if not dfs(node, root):
                    return False

            return True

        return dfs() and len(visited) == n


res = Solution().validTree(
    n=5,
    edges=[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
)
print(res)
