# LC 347 Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        # list of (数, 次数)，按次数降序
        items = sorted(counts.items(), key=lambda item: item[1], reverse=True)

        ans = []
        for i in range(k):
            pair = items[i]
            ans.append(pair[0])
        return ans
