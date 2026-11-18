# LC 224 Basic Calculator
# https://leetcode.com/problems/basic-calculator/
# 参考答案（讲解时给出），只适用于只有 + - 和括号

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        sign = 1
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                res = res + sign * num
                continue
            elif c == '+':
                sign = 1
            elif c == '-':
                sign = -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                outer_sign = stack.pop()
                outer_res = stack.pop()
                res = outer_res + outer_sign * res
            i += 1
        return res
