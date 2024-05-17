'''
Problem: Partition Labels
Link: https://leetcode.com/problems/partition-labels/description/
Tags: Two Pointer, Hash Table, String
'''


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        res = []
        ch = {c: i for i, c in enumerate(s)}

        start = last = 0
        for i, c in enumerate(s):
            last = max(last, ch[c])
            if last == i:
                res.append(last - start + 1)
                start = last + 1

        return res


res = Solution().partitionLabels(
    "ababcbacadefegdehijhklij"
)

print(res)
