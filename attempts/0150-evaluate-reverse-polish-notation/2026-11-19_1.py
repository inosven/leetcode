# LC 150 Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# 日期: 2026-11-19 | 章节: 栈与队列 | 结果: B | 用时: 5min

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        n=len(tokens)
        i=0
        
        while i < n:
            if tokens[i].isdigit():
                st.append(int(tokens[i]))
                i+=1
            else:
                b = st.pop()
                a = st.pop()
                if  tokens[i] == '+':
                    val = a + b       
                elif  tokens[i] == '-':
                    val = a - b       
                elif  tokens[i] == '*':
                    val = a * b       
                elif  tokens[i] == '/':
                    val = int(a / b)
                st.append(val)
        return st[-1]
