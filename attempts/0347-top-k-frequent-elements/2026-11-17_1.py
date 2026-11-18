# LC 347 Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# 日期: 2026-11-17 | 章节: 栈与队列 | 结果: B | 用时: 30min

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] = counts.get(num,0) + 1
        cton = defaultdict(list)
        for num,count in counts.items():
            cton[count].append(num)
        
        list_count = list(counts.values())
        list_count.sort(reverse=True)
        ans = []
        i=0
        for i in range(k):
            for num in cton[list_count[i]]:
                ans.append(num)
                if len(ans) == k:
                    return ans
