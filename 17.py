class Solution:
    dg_chs = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == '': 
            return []

        res = []
        next_dgs = digits[1:]
        curr_dg = int(digits[0])

        for c in self.dg_chs[curr_dg]:
            suffixes = self.letterCombinations(next_dgs)
            if suffixes == []:
                res += [c]
                continue
            for suffix in suffixes:
                res += [c + suffix]
        
        return res

res = Solution().letterCombinations(
    digits="23"
)
print(res)
