# LC 236 Lowest Common Ancestor of a Binary Tree

## 2026-11-17 · B · 15min

- 层级：实现错。后序遍历 + 左右都找到返回 node / node 是 p 或 q 返回 node / 单边上传，思路和定义都对。
- Bug：`right = postorder(node.left, p, q)` 复制粘贴没改成 `node.right`，右子树从没被访问（常犯：递归调用传错变量）。
- 反例：`[1, null, 2, 3]`, p=2, q=3 → 根的 left/right 都是 post(None)=None，返回 None，应为 2。样例 `[3,5,1,...]` p=5,q=1 碰巧过（left、right 都算成 5，非空 → 返回 3）。
- invariant：post(node) = 子树里 p、q 都在则返回 LCA，只有一个则返回它，都没有返回 None；成立前提是 left/right 分别覆盖两棵不同子树。
- 口诀：复制出来的对称行，逐个核对左右是不是都换过来了。
