import string

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        
        n = len(p)
        pc = {x: 0 for x in string.ascii_lowercase}
        for c in p:
            pc[c] += 1

        ac = {x: 0 for x in string.ascii_lowercase}
        for c in s[:n]:
            ac[c] += 1

        for right in range(n, len(s)):
            if ac == pc:
                res.append(left)
            
            # Shift window
            left = right - n
            ac[s[right]] += 1
            ac[s[left]]  -= 1
            left += 1
        
        # In case the last window is not computed
        if ac == pc:
            res.append(left)
        
        return res

res = Solution().findAnagrams(
    s="abab",
    p="ab"
)
print(res)
