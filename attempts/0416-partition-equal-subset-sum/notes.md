# LC 416 Partition Equal Subset Sum

## 2026-11-17 · B · 25min

### 版本 1（二维）
- Bug 1（实现错，第一个出错点）：`if j > nums[i-1]` 少了等号，漏掉"只取这一个数凑出 j"。反例 `[1,1]` → False，应为 True。
- Bug 2（定义错）：`dp[i][j-nums[i-1]]` 应为 `dp[i-1][...]`。看本行 = 同一个数可重复取（完全背包），违反"前 i 个数，每个最多一次"。反例（修好 Bug 1 后）`[1,3]`：dp[1][2] = dp[1][1] = T（1 用两次）→ True，应为 False。
- 死代码：`if all(nums) is 0` —— 他想判断"全是 0"，但 `all(nums)` 是"都不为 0"，`is` 比较对象不比较值（`False is 0` 恒 False）。全 0 本来就由 `dp[i][0] = True` 覆盖（target=0）。
- 他担心 `dp[i][0]` 被 `dp[0][j] = False` 覆盖：那个循环从 j=1 开始，碰不到第 0 列。

### 版本 2（一维）
- Bug：`range(target+1, ...)` 起点越界（dp 最大下标 target），总和为偶数的输入都会 IndexError。改 `range(target, nums[i-1]-1, -1)`。倒序和下界都写对了。
- 倒序 invariant：更新 dp[j] 时 dp[j-x] 本轮还没改，仍是上一行 = 二维的 `dp[i-1][j-x]`；正序就退化成版本 1 的 Bug 2。

- 口诀：0/1 背包看上一行，完全背包看本行；`j == x` 表示只拿这一个数，等号不能漏。`range` 起点闭（要是合法下标）、终点开（写想要的最小值 - 1）。加特判前先用这个输入跑一遍 base case。
