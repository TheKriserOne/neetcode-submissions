# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        if head is None:
            return head
        while temp and temp.next:
            if prev is None:
                prev = temp
                temp = temp.next
                prev.next = None
            else:
                a = temp.next
                temp.next = prev
                prev = temp
                temp = a 
        temp.next = prev
        return temp



        