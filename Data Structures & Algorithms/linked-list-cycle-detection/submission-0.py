# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if slow is None or slow.next is None:
            return False
        fast = head.next
        while slow != fast:
            slow = slow.next
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next       
        return True
        