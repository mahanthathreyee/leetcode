'''
Problem: Find the Duplicate Number
Link: https://leetcode.com/problems/find-the-duplicate-number/description/
Tags: Array, Two Pointers, Hare Algorithm
'''


class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[slow]

        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]

        return slow


res = Solution().findDuplicate(
    nums=[1, 3, 4, 2, 2]
)
print(res)
