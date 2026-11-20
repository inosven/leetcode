# LC 209 Minimum Size Subarray Sum

## 2026-11-19 · A · 10min

- 一遍过。滑动窗口，O(n)。
- invariant：while 每次检查前 total == sum(nums[left..right])；和够了就记长度再收缩左端。
- `left <= right` 多余：target >= 1 且元素为正，窗口空时 total = 0 < target，while 自然停。
