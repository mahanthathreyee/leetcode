'''
Problem: Number of Connected Components in an Undirected Graph
Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/ # noqa: E501
Tags: DFS, BFS, Components
'''

from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        adj_edge = defaultdict(list)
        for x, y in edges:
            adj_edge[x].append(y)
            adj_edge[y].append(x)

        visited = set()

        def dfs(root):
            visited.add(root)

            for node in adj_edge[root]:
                if node not in visited:
                    dfs(node)

        ans = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                ans += 1

        return ans


res = Solution().countComponents(
    n=6,
    edges=[[0, 1], [1, 2], [2, 3], [4, 5]]
)
print(res)
