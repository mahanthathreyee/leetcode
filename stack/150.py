'''
Problem: Evaluate Reverse Polish Notation
Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
Tags: Stack, Array
'''

class Solution:
    evaluator = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(x / y),
    }

    def evalRPN(self, tokens: list[str]) -> int:
        st = []
        for token in tokens:
            if len(token) == 1 and ord(token) < 48:
                y = st.pop()
                x = st.pop()
                token = Solution.evaluator[token](x, y)
            st.append(int(token))
        
        return st[0]

res = Solution().evalRPN(
    ["2","1","+","3","*"]
)
print(res)
