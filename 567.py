class Solution:
    def checkInclusion(self, A: str, B: str) -> bool:
        def ord_c(x: str) -> int:
            return ord(x) - 97
        
        def get_c_freq(S: str) -> list[int]:
            s_c = [0] * 26
            for c in S:
                s_c[ord_c(c)] += 1
            return s_c
        

        a_c = get_c_freq(A)
        x = set(A)
        n = len(A)

        left = 0
        for right, c in enumerate(B):
            a_c[ord_c(c)] -= 1
            if c not in x:
                while left <= right:
                    a_c[ord_c(B[left])] += 1
                    left += 1
                continue
            while right - left >= n:
                a_c[ord_c(B[left])] += 1
                left += 1

            if sum(a_c) == 0 and min(a_c) == 0:
                return True

        return False

res = Solution().checkInclusion(
    A="adc",
    B="dcda"
)
print(res)
