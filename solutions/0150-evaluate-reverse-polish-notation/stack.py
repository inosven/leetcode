# LC 150 Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        n = len(tokens)
        i = 0

        while i < n:
            # 运算符只有 4 个；其余都是数字（可能是负数）
            if tokens[i] not in ('+', '-', '*', '/'):
                st.append(int(tokens[i]))
                i += 1
            else:
                b = st.pop()
                a = st.pop()
                if tokens[i] == '+':
                    val = a + b
                elif tokens[i] == '-':
                    val = a - b
                elif tokens[i] == '*':
                    val = a * b
                elif tokens[i] == '/':
                    val = int(a / b)   # 向 0 截断
                st.append(val)
                i += 1
        return st[-1]
