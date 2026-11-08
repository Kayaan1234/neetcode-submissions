# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # 1. Temporarily save the next node
            curr.next = prev       # 2. Reverse the current node's pointer
            prev = curr            # 3. Move 'prev' one step forward
            curr = next_node       # 4. Move 'curr' one step forward
            
        return prev  # 'prev' will be the new head of the reversed list
