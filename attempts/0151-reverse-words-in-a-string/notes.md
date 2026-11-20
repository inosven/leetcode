# LC 151 Reverse Words in a String

## 2026-11-19 · B · 15min

- 层级：实现错 ×3（思路对：整体反转 + 逐词反转）。根因：单词边界 [start, i] 没写对。
- Bug 1（第一个出错点）：`reverseS[i:i+1]` 只切一个字符，存了 start 没用，应为 `[start:i+1]`。反例 "ab cd" → "c "。
- Bug 2：内层 while 的 `or i==n-1` 让 i 越过结尾到 n，最后一个单词切成 ""。
- Bug 3：开头判断缺 `reverseS[i] != ' '`；strip 只去首尾，中间连续空格时会从空格起词。反例 "a··b"。
- 追问：去掉 `or i==n-1` 不会漏最后一个单词：while 只负责停在哪，停在 n-1 后照常切片。
- invariant：内层 while 结束时 i 停在当前单词最后一个字符。
- 口诀：存了 start 就要用上 start，切片 = [start, 当前位置 + 1)；while 只管停在哪，处理在 while 之后。
