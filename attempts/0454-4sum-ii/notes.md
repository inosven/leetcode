# LC 454 4Sum II

## 2026-11-14 · A · 15min

- 代码正确，O(n²)。
- invariant：`count[s]` = 从 nums1、nums2 各取一个和为 s 的取法数；左右配对用乘法原理 `c * count2[-s]`。
- 小问题：`defaultdict(int)` 和 `.get(s,0)+1` 重复，二选一，直接 `count[s] += 1`。
- 查询用 `.get(-s, 0)` 而不是 `[]`：defaultdict 的 `[]` 会插入新 key，边遍历边查同一个字典时会 RuntimeError。
- 口诀：四数拆两两，存和的次数，查相反数，次数相乘。
