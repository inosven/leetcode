# LC 224 Basic Calculator
# https://leetcode.com/problems/basic-calculator/

class Solution:
    def calculate(self, s: str) -> int:
        priority = {'+': 1, '-': 1, '*': 2, '/': 2}
        ops = []
        nums = []
        s = s.replace(' ', '')

        def calstack():
            b = nums.pop()
            a = nums.pop()
            op = ops.pop()
            if op == '+':
                val = a + b
            elif op == '-':
                val = a - b
            elif op == '*':
                val = a * b
            elif op == '/':
                val = int(a / b)   # 向 0 截断
            nums.append(val)

        n = len(s)
        i = 0
        while i < n:
            if s[i] == "(":
                ops.append(s[i])
                i += 1
            elif s[i] == ")":
                while ops[-1] != '(':
                    calstack()
                ops.pop()
                i += 1
            elif s[i].isdigit():
                num = int(s[i])
                while i + 1 < n and s[i + 1].isdigit():
                    num = num * 10 + int(s[i + 1])
                    i += 1
                nums.append(num)
                i += 1
            else:
                # 一元负号：开头或紧跟 '(' 时补 0
                if s[i] == '-' and (i == 0 or (i - 1 >= 0 and s[i - 1] == '(')):
                    nums.append(0)
                # '(' 是墙：不越过它，也不查它的优先级
                while ops and ops[-1] != '(' and priority[s[i]] <= priority[ops[-1]]:
                    calstack()
                ops.append(s[i])
                i += 1
        while ops:
            calstack()
        return nums[-1]
