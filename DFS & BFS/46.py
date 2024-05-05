'''
Problem: Permutations
Link: https://leetcode.com/problems/permutations/
Tags: DFS, Combination
'''

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def dfs(nums: set, path: list=list()):
            if not nums:
                res.append(path)
                return 
            for x in nums:
                dfs(nums - {x}, path + [x])
        
        dfs(set(nums))
        return res

res = Solution().permute(
    [1,2,3]
)
print(res)
