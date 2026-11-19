# LC 454 4Sum II

## 2026-11-14 · A · 15min

- 代码正确，O(n²)。
- invariant：`count[s]` = 从 nums1、nums2 各取一个和为 s 的取法数；左右配对用乘法原理 `c * count2[-s]`。
- 小问题：`defaultdict(int)` 和 `.get(s,0)+1` 重复，二选一，直接 `count[s] += 1`。
- 查询用 `.get(-s, 0)` 而不是 `[]`：defaultdict 的 `[]` 会插入新 key，边遍历边查同一个字典时会 RuntimeError。
- 口诀：四数拆两两，存和的次数，查相反数，次数相乘。

## 2026-11-19 · A · 10min

- 结果正确，O(n²)。问"为什么慢"：常数大。
  1. 存 `(i,j)` 下标列表，但只用 `len()` → n² 个 tuple + list；只问个数就存 `defaultdict(int)` 计数。
  2. `sumtoi[target]` 在 defaultdict 上查找会插入空 list，最多多插 n² 个 key；改 `.get(target, 0)`。
- 复杂度下界：两两分组 O(n²) 已是最优，1+3 分组是 n³。
- 口诀：只问个数就只存个数；用 defaultdict 查找时要用 `.get`，不要用 `[]`。
