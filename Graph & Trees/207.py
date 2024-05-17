'''
Problem: Course Schedule
Link: https://leetcode.com/problems/course-schedule/description/
Tags: DFS, Graph, Topological Ordering
'''

from collections import defaultdict


class Solution:
    def canFinish(self, n: int, preq: list[list[int]]) -> bool:
        deg = [0] * n
        adj = defaultdict(list)
        for x, y in preq:
            adj[x].append(y)
            deg[y] += 1

        c_fin = [i for i in range(n) if deg[i] == 0]

        for i in c_fin:
            for j in adj[i]:
                deg[j] -= 1
                if deg[j] == 0:
                    c_fin.append(j)

        return n == len(c_fin)


res = Solution().canFinish(
    n=5,
    preq=[[1, 4], [2, 4], [3, 1], [3, 2]]
)
print(res)
