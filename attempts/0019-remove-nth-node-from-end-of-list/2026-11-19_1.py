# LC 19 Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# 日期: 2026-11-19 | 章节: 链表 | 结果: A | 用时: 5min

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        fast = dummy_head
        slow = dummy_head

        for _ in range(n+1):
            fast = fast.next
        
        while fast:
            fast=fast.next
            slow =slow.next
        
        slow.next = slow.next.next
        return dummy_head.next
