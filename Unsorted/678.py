class Solution:
    def checkValidString(self, s: str) -> bool:
        st = []
        op = 0

        for c in s:
            if c == '(' or c == '*':
                op += 1
                
                if c == '(': st.append(c)
                elif st: st.pop()
            else:
                if st: st.pop()
                op -= 1
            
            if op < 0: return False
        
        return st == []
    
res = Solution().checkValidString(
    s="((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
)
print(res)