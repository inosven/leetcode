# LC 40 Combination Sum II

## 2026-11-19 · A · 15min

- 一遍过。排序 + 回溯，同层去重 `i > start`（不是 `i > 0`），和超了 `break`（排序后单调）。
- `s == target` 后没 return：不影响结果，因为 candidates >= 1，下一层循环第一步就 break；加 `return` 更清楚。
