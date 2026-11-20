# LC 151 Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/
# 整体反转，再逐个单词反转。单词 = [start, i]：开头是非空格且前一个为空格或 i==0；
# 内层 while 停在单词最后一个字符。O(n)

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
            if reverseS[i] != ' ' and ((i-1>=0 and reverseS[i-1] == ' ') or i==0):
                start = i
                while (i+1 < n and reverseS[i+1]!=' '):
                    i+=1
                cur = reverse(reverseS[start:i+1])
                ans.append(cur)
            i+=1
        return ' '.join(ans)
