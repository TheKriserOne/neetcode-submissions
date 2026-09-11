# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        head = merged
        temp = list1
        temp2 = list2
        while temp or temp2:
            if temp is not None and temp2 is not None:
                if temp.val <= temp2.val:
                    merged.next = temp
                    temp= temp.next
                    merged = merged.next
                else:
                    merged.next = temp2
                    temp2 = temp2.next
                    merged = merged.next                    
            elif temp is None:
                merged.next = temp2
                temp2 = temp2.next
                merged = merged.next         
            else:
                merged.next = temp
                temp = temp.next
                merged = merged.next
        return head.next

        
        
        