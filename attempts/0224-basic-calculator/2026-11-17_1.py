# LC 224 Basic Calculator
# https://leetcode.com/problems/basic-calculator/
# 日期: 2026-11-17 | 章节: 栈与队列 | 结果: C | 第 1 版（思路错：把 150 的后缀做法套到中缀）

class Solution:
    def calculate(self, s: str) -> int:
        PAR = ['(',')']
        DIGITS = ['1','2','3','4','5','6','7','8','9','0' ]
        stack = []
        
        while stack:
            if s[i] in DIGITS:
                stack.append(s[i])
                i+=1
            if s[i]=='(':
                temp = []
                i+=1
                while s[i] != ')':
                        temp.append(s[i])
                        i+=1
                    for j in range(temp):
                        if s[i] =='+' or s[i] =='-':
                            b = temp.pop()
                            a = temp.pop()
                            if s[i] =='+':
                                ans = a + b
                            else:
                                ans = a - b
                            temp.append(ans)
                            i+=1
                total = temp.pop()
                stack.append(total)
        return stack.pop()
