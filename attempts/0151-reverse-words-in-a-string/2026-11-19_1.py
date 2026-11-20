# LC 151 Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/
# 日期: 2026-11-19 | 章节: 字符串 | 结果: B | 用时: 15min

class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(s):
            left =0
            right = len(s)-1
            lst = list(s)
            while left<right:
                lst[left],lst[right] = lst[right],lst[left]
                left+=1
                right-=1
            return ''.join(lst)
        
        s = s.strip()
        reverseS = reverse(s)
        n = len(reverseS)
        i=0
        ans = []
        while i < n:
            if (i-1>=0 and reverseS[i-1] == ' ') or i==0:
                start = i
                while (i+1 < n and reverseS[i+1]!=' ') or i==n-1:
                    end = i
                    i+=1
                cur = reverse(reverseS[i:i+1])
                ans.append(cur)
            i+=1
        return ' '.join(ans)
