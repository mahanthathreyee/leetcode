'''
Problem: 3 Sum
Link: https://leetcode.com/problems/3sum/description/
Tags: Binary Search, Two Pointer, Sorting
'''

class Solution:
    def threeSum(self, A: list[int]) -> list[list[int]]:
        res = []
        A.sort()
        n = len(A)

        i = 0
        while i < n:
            target = -A[i]
            beg = i + 1
            end = n - 1

            while beg < end:
                s = A[beg] + A[end]
                
                if   s < target: beg += 1
                elif s > target: end -= 1
                else:
                    triplet = [A[i], A[beg], A[end]]
                    res.append(triplet)

                    while beg < end and A[beg] == triplet[1]: beg += 1
                    while beg < end and A[end] == triplet[2]: end -= 1

            while i + 1 < n and A[i] == A[i + 1]: i += 1
            i += 1

        return res

res = Solution().threeSum(
    [-1,0,1,2,-1,-4]
)
print(res)
