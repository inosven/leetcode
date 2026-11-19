# LC 772 Basic Calculator III (Premium)
# https://leetcode.com/problems/basic-calculator-iii/
# 日期: 2026-11-19 | 章节: 栈与队列 | 结果: C | 用时: 30min

class Solution:
    def calculate(self, s: str) -> int:
        priority =  {'+':1,'-':1,'*':2,'/':2}
        ops=[]
        nums = []
        s = s.replace(' ', '')
        def calstack():
            b = nums.pop()
            a = nums.pop()
            op = ops.pop()
            if op =='+':
                val = a + b
            elif op =='-':
                val = a - b
            elif op == '*':
                val = a * b
            elif op == '/':
                val = int(a/b)
            nums.append(val)
            return 
        
        n = len(s)
        i=0
        while i < n:
            if s[i] == "(":
                ops.append(s[i])
                i+=1
            elif s[i] == ")":
                while ops[-1] != '(':
                    calstack()
                ops.pop()
                i+=1
            elif s[i].isdigit():
                num = int(s[i])
                while i+1 < n-1 and s[i+1].isdigit():
                    num = num*10+ int(s[i])
                    i+=1
                nums.append(num)
                i+=1
            else:
                if s[i]=='-' and (i==0 or (i-1> 0 and s[i-1]=='(')):
                    nums.append(0)
                while ops and priority[s[i]] <= priority[ops[-1]]:
                    calstack()
                ops.append(s[i])
                i+=1
        while ops:
            calstack()
        return nums[-1]
