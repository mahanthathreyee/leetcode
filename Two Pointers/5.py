'''
Problem: Longest Palindromic Substring
Link: https://leetcode.com/problems/longest-palindromic-substring/
Tags: Two Pointer, Dynamic Programming, String
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = [-1, -1]

        for i, x in enumerate(s):
            right = i
            while right < n and s[right] == x:
                right += 1
            
            left = i - 1
            while left >= 0 and right < n and s[left] == s[right]:
                right += 1
                left -= 1

            pal_len = right - left - 1
            if res[1] < pal_len:
                res[0] = left + 1
                res[1] = pal_len
        
        return s[res[0] : sum(res)]

res = Solution().longestPalindrome(
    "babad"
)
print(res)
