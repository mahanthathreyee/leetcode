class Solution:
    def maxDistance(self, A: list[int], B: list[int]) -> int:
        res = 0
        left, right = 0, 0
        while left < len(A) and right < len(B):
            if A[left] > B[right]:
                left += 1
            else:
                res = max(res, right - left)
                right += 1

        return res


res = Solution().maxDistance(
    A=[30, 29, 19, 5],
    B=[25, 25, 25, 25, 25]
)
print(res)
