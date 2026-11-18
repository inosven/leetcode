# LC 347 Top K Frequent Elements

## 2026-11-17 · B · 30min

- 层级：定义错。`list_count = list(counts.values())` 是"每个数一个频次"（有重复），但遍历时每个 i 取走一整个桶 `cton[list_count[i]]`，当成了"不重复的频次"→ 同频次的桶被重复取。
- 反例：`[1,1,2,2,3]`, k=3 → `list_count=[2,2,1]`，i=0 取 [1,2]，i=1 又取 [1,2] → `[1,2,1]`，应为 `[1,2,3]`。
- 修改：`list_count = list(cton.keys())`。range(k) 不会越界：每桶 ≥1 个数，最多 k 个桶就凑满。
- 杂项：`defaultdict(int)` 和 `.get(num, 0)` 混用（重复保护）；`i = 0` 多余。
- 追问：`dict.get(key, default)` 计数写法（普通 dict）；`sorted(counts.items(), key=lambda item: item[1], reverse=True)` 返回 list of tuples（`.items()` 产生 tuple，`sorted` 永远返回 list），取 `items[i][0]`；默认升序要 `reverse=True`。
- 复杂度：对频次 sort 是 O(m log m)；真正 O(n) 桶排序是按频次下标开数组（频次 ≤ n）从大往小扫。
- 口诀：已经按 key 分好组的数据，遍历时要遍历 key，不要遍历原始元素。
