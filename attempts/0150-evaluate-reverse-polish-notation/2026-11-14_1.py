# LC 150 Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# 日期: 2026-11-14 | 章节: 栈与队列 | 结果: B（bug 未自己发现）| 用时: 10min

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operations = ['+', '-', '*', '/']
        print(tokens)

        for t in tokens:
            if t not in operations:
                st.append(t)
            else:
                b = st.pop()
                a = st.pop()
                if t =="+":
                    temp = a+b
                    st.append(temp)
                elif t =="-":
                    temp = a-b
                    st.append(temp)
                elif t =="*":
                    temp = a*b
                    st.append(temp)
                elif t =="/":
                    temp = a//b
                    st.append(temp)
        return st.pop()
