# LC 19 Remove Nth Node From End of List

## 2026-11-14 · A · 5min

- 代码正确（小 bug 自己调通）。
- invariant：`fast` 先走 n 步后两指针同步走，`fast` 始终领先 `slow` n 步；`while fast.next` 停时 `fast` 在最后一个节点，`slow` 在倒数第 n+1 个，即要删节点的前驱。
- `dummyHead` 让「删头节点」也有前驱，所以返回 `dummyHead.next` 而不是 `head`。
- 担心是背会的，自测题：
  1. 改成 `while fast`，`fast` 先走几步？
  2. 不用 dummy、从 `head` 出发，`[1,2], n=2` 会怎样？
  3. 只返回倒数第 n 个节点（不删），改哪几行？
- 口诀：删节点找前驱；前驱可能不存在就加 dummy。

## 2026-11-19 · A · 5min

- 一遍对。dummy 出发、fast 先走 n+1 步、`while fast`，slow 停在被删节点的前一个；`[1], n=1` 时删头节点也对。
