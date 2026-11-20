# LC 131 Palindrome Partitioning

## 2026-11-19 · B · 15min

- 层级：实现错（老毛病：递归传固定参数）。`bt(start+1)` 应为 `bt(i+1)`。
- 反例 "aa"：切下 "aa" 后 bt(1) 又切一个 "a"，得到 ["aa","a"]。
- invariant：bt(start) 表示 s[0:start] 已切好；本层切 s[start:i+1]，下一层从 i+1 开始。
- 口诀：切到哪，下一层就从哪的下一位开始，传 i+1，不传 start+1。
