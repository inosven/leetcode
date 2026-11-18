# LC 347 Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        # cton: 频次 -> 有这个频次的所有数
        cton = defaultdict(list)
        for num, count in counts.items():
            cton[count].append(num)

        # 遍历不重复的频次，从大到小，一次取一个桶
        list_count = list(cton.keys())
        list_count.sort(reverse=True)
        ans = []
        for i in range(k):
            for num in cton[list_count[i]]:
                ans.append(num)
                if len(ans) == k:
                    return ans
