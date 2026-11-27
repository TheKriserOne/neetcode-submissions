# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        temp = head
        traverse = head
        prev = None
        for i in range(n):
            traverse = traverse.next
        while traverse:
            prev = temp
            temp = temp.next
            traverse = traverse.next
        if prev is None:
            head = temp.next
            return head
        prev.next = temp.next

        return head

        