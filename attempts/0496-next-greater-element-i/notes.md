# LC 496 Next Greater Element I

## 2026-11-14 · B · 10min

- （本次代码未存档）Bug：把整个 nums2 压栈，而不是 nums2[i]。与 739 同类：栈里放错东西。

## 2026-11-19 · B · 10min

- 层级：实现错 ×3（思路对：单调递减栈 + nums1 值→下标映射）。
- Bug 1（第一个出错点）：`num = st.pop` 少了括号，拿到方法对象、栈没变 → while 死循环。反例 `nums1=[1], nums2=[1,2]`。
- Bug 2：`ntoi.get(num2)` 应查被弹出的 `num`。
- Bug 3：`ans[pos] = num` 应填 `num2`。Bug 2、3 是 num/num2 角色互换（变量名混淆老毛病）。
- invariant：栈里是还没找到下一个更大元素的数，栈底→栈顶递减；num2 弹出栈顶即为其答案。
- 口诀：弹出的是"填谁"，弹它的是"填什么"。

## 2026-11-19 · A · 5min（当天重做）

- 一遍过，与 solution 一致。三处 bug（pop 括号、查 num、填 num2）都改对了。
