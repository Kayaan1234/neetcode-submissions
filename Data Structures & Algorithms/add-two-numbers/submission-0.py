# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # 2. Loop until both lists are empty AND there is no remaining carry
        while l1 or l2 or carry:
            # Get values from current nodes, default to 0 if list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the total sum for this position
            total = val1 + val2 + carry
            
            # Update carry and calculate the digit to store
            carry = total // 10
            digit = total % 10
            
            # Create a new node with the digit and move the pointer forward
            current.next = ListNode(digit)
            current = current.next
            
            # Move to the next nodes in the input lists if they exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        # 3. Return the head of the new list (skipping the dummy node)
        return dummy.next

            

            