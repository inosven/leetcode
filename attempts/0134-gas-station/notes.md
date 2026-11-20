# LC 134 Gas Station

## 2026-11-19 · A · 15min

- 一遍过。贪心，O(n)。
- invariant：total = 从 ans 到 i 的累计剩油。在 i 处变负 → 从 [ans, i] 任一点出发到 i 都会断（前缀非负，去掉只会更少），起点跳到 i+1。
- 全局 sum(gas) >= sum(cost) 时一定有解，最后的 ans 不用再绕回检查。
- 小点：diff 数组、sumgas/sumcost 可合成一个 totalAll += gas[i] - cost[i]，不影响正确性。
