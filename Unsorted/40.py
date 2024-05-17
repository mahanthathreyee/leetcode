'''
Problem: Combination Sum II
Link: https://leetcode.com/problems/combination-sum-ii/description/
Tags: Backtracking, Array
'''


class Solution:
    def combinationSum2(self, A: list[int], target: int) -> list[list[int]]:
        def solve(curr, target, result, path=[]):
            if not target:
                result.append(path)
                return

            for i in range(curr, n):
                if i > curr and A[i-1] == A[i]:
                    continue
                if A[i] > target:
                    break

                solve(i + 1, target - A[i], result, path + [A[i]])

        n = len(A)
        A.sort()
        result = []
        solve(0, target, result)
        return result


res = Solution().combinationSum2(
    A=[10, 7, 6, 5, 2, 1, 1],
    target=8
)
print(res)
