# LC 150 Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operations = ['+', '-', '*', '/']

        for t in tokens:
            if t not in operations:
                st.append(int(t))
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
                    temp = int(a / b)
                    st.append(temp)
        return st.pop()
