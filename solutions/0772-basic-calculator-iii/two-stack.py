# LC 772 Basic Calculator III (Premium)
# https://leetcode.com/problems/basic-calculator-iii/
# 无会员未在 LC 提交；本地随机对拍通过
# 双栈：数字栈 + 运算符栈 + 优先级。比较看栈顶 ops[-1]，'(' 是墙；一元负号补 0。O(n) / O(n)

class Solution:
    def calculate(self, s: str) -> int:
        precedence = {'+':1,'-':1,'*':2,'/':2}

        ops = []
        nums = []

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
                val = int(a / b)
            nums.append(val)
            return

        s = s.replace(' ','')
        n = len(s)
        i=0


        while i < n:
            if s[i] == "(":
                ops.append(s[i])
                i+=1
            elif s[i] == ")":
                while ops[-1] != "(":
                    calstack()
                ops.pop()
                i+=1
            elif s[i].isdigit():
                num = int(s[i])
                while i+1 < n and s[i+1].isdigit():
                    num = num*10 + int(s[i+1])
                    i+=1
                nums.append(num)
                i+=1
            else:
                if s[i] == '-':
                    if (i>0 and s[i-1] =='(') or i==0:
                        nums.append(0)
                while ops and ops[-1]!='(' and precedence[s[i]] <= precedence[ops[-1]]:
                        calstack()
                ops.append(s[i])
                i+=1
        while ops:
            calstack()
        
        return nums[-1]
