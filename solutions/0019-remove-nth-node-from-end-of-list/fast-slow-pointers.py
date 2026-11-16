# LC 19 Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode(next=head)

        fast = dummyHead
        slow = dummyHead

        for _ in range(n):
            fast=fast.next
        
        while fast.next:
            fast=fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummyHead.next
