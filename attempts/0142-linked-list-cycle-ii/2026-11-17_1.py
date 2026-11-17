# LC 142 Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/
# 日期: 2026-11-17 | 章节: 链表 | 结果: B | 用时: 10min

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if slow is not fast:
            return -1

        pointer = head

        while slow is not pointer:
            pointer = pointer.next
            slow = slow.next
        return slow
