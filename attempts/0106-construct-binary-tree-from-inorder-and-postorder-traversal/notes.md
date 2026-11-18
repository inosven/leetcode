# LC 106 Construct Binary Tree from Inorder and Postorder Traversal

## 2026-11-17 · B · 10min

- 层级：定义错 + 实现错。思路（后序末尾是根 → 中序里找根 → 切左右递归）、`left_size`、`postorder[left_size:-1]` 都对。
- Bug 1（第一个出错点）：`inorder[:mid]` 用了值 `mid` 当下标，应为 `mid_pos`（变量名混淆）。例：根 3 → `inorder[:3]` = [9,3,15]，应为 [9]。
- Bug 2（根因，定义错）：`ntoi` 存原数组的全局下标，但 `build` 收到的是切片（局部下标）。右子树 `[15,20,7]` 里 20 的全局下标 3、局部下标 1。改 `mid_pos = inorder.index(mid)`（O(n²)），或不切片改传 `[l, r]` 区间、保留 ntoi（O(n)）。
- Bug 3：无递归出口，空列表 `postorder[-1]` IndexError → `if not postorder: return None`。
- invariant：`build` 收到的两个列表是同一棵子树的两种遍历，下标从 0 开始。
- 口诀：切片用局部下标，传区间用全局下标；哈希表存的是哪种下标，就只能在那种坐标里用。
