# LC 131 Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/
# 日期: 2026-11-19 | 章节: 回溯 | 结果: B | 用时: 15min

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        def isP(s):
            left = 0
            right = len(s)-1
            while left < right:
                if s[left] == s[right]:
                    left+=1
                    right-=1
                    continue
                else:
                    return False
            return True
        
        path = []
        ans = []
        def bt(start):
            if start==n:
                ans.append(path[:])
            for i in range(start,n):
                cur = s[start:i+1]
                if isP(cur):
                    path.append(cur)
                    bt(start+1)
                    path.pop()
                else:
                    continue
        
        bt(0)
        return ans
