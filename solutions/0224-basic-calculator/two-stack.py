# LC 224 Basic Calculator
# https://leetcode.com/problems/basic-calculator/

class Solution:
    def calculate(self, s: str) -> int:
        s=s.replace(' ','')
        n=len(s)

        DIGITS = ['1','2','3','4','5','6','7','8','9','0' ]
        priority = {'+':1, '-':1, '*':2, '/':2}
        st_op = []
        st_num = []
        def cal_stack():
            b = st_num.pop()
            a = st_num.pop()
            op = st_op.pop()
            if op == '+':
                val = a + b
            else:
                val = a - b
            st_num.append(val)
            return

        i=0
        while i < len(s):
            c = s[i]
            if c =='(':
                st_op.append(c)
                i+=1
            elif c ==')':
                while st_op[-1] != '(':
                    cal_stack()
                st_op.pop()
                i+=1
            elif c in DIGITS:
                val = int(c)
                while i+1 < n and s[i + 1] in DIGITS:
                    val = val*10 + int(s[i + 1])
                    i+=1
                st_num.append(val)
                i+=1
            else:
                if c =='-':
                    if i==0 or (i>0 and s[i-1]) =='(':
                        st_num.append(0)
                while st_op and st_op[-1] != '(' and priority[st_op[-1]] >= priority[c]:
                    cal_stack()
                st_op.append(c)
                i+=1

        while st_op:
            cal_stack()
        
        return st_num.pop()
