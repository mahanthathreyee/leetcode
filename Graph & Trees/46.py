'''
Problem: Permutations
Link: https://leetcode.com/problems/permutations/
Tags: DFS, Combination
'''


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def dfs(nums: set, path: list):
            if not nums:
                ans.append(path)
                return
            for x in nums:
                dfs(nums - {x}, path + [x])

        dfs(set(nums), [])
        return ans


res = Solution().permute(
    [1, 2, 3]
)
print(res)
