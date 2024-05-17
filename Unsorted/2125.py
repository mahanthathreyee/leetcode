class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        def stringSum(row: str):
            return sum([int(x) for x in row])

        res = 0
        pre = 0
        for row in bank:
            nex = stringSum(row)
            if nex:
                res, pre = res + (pre * nex), nex
        return res


res = Solution().numberOfBeams([
    "011001",
    "000000",
    "010100",
    "001000"
])
print(res)
