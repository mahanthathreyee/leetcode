'''
Problem: Search in Rotated Sorted Array
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
Tags: Binary Search, Array
'''


class Solution:
    def search(self, A: list[int], target: int) -> int:
        beg = 0
        end = len(A)

        while beg < end:
            mid = (beg + end) // 2

            if target < A[0] < A[mid]:
                beg = mid + 1
            elif target >= A[0] > A[mid]:
                end = mid
            elif target > A[mid]:
                beg = mid + 1
            elif target < A[mid]:
                end = mid
            else:
                return mid

        return -1


res = Solution().search(
    A=[4, 5, 6, 7, 0, 1, 2],
    target=0
)
print(res)
