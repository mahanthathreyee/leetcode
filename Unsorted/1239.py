class Solution:
    def maxLength(self, A):
        dp = [set()]
        for a in A:
            if len(set(a)) < len(a):
                continue
            a = set(a)
            for c in dp[:]:
                if a & c:
                    continue
                dp.append(a | c)

            print(dp)
        return max(len(a) for a in dp)


print(Solution().maxLength(
    ["cha", "r", "act", "ers"]
))

# cdefghabxyz
