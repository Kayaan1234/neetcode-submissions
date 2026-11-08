class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[0]
        
        while True:
            tortoise = nums[tortoise]          # Moves 1 step
            hare = nums[nums[hare]]            # Moves 2 steps
            if tortoise == hare:
                break
                
        # Phase 2: Find the entrance to the cycle (the duplicate number)
        tortoise = nums[0]                     # Reset tortoise to start
        while tortoise != hare:
            tortoise = nums[tortoise]          # Both move 1 step now
            hare = nums[hare]
            
        return tortoise