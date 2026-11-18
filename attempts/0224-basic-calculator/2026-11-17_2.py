# LC 224 Basic Calculator
# https://leetcode.com/problems/basic-calculator/
# 日期: 2026-11-17 | 章节: 栈与队列 | 结果: C | 第 2 版（看答案后改用双栈；bug: for+enumerate 里改 i、空格、op/st_op）

class Solution:
    def calculate(self, s: str) -> int:
        s=s.strip()
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


        for i,c in enumerate(s):
            if c =='(':
                op.append(c)
            elif c ==')':
                while st_op[-1] != '(':
                    cal_stack()
                st_op.pop()
            elif c in DIGITS:
                val = int(c)
                while i+1 < n and s[i + 1] in DIGITS:
                    val = val*10 + int(s[i + 1])
                    i+=1
                st_num.append(val)
            else:
                if c =='-':
                    if i==0 or (i>0 and s[i-1]) =='(':
                        st_num.append(0)
                while st_op and st_op[-1] != '(' and priority[st_op[-1]] >= priority[c]:
                    cal_stack()
                st_op.append(c)

        while st_op:
            cal_stack()
        
        return st_num.pop()
