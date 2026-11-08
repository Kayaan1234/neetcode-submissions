class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        prefix = [0 for i in range(len(nums))]
        postfix = [0 for i in range(len(nums))]
        output = [0 for i in range(len(nums))]
        prefix[0] = nums[0]
        postfix[-1] = nums[-1]
        for i in range(1, len(nums), 1):
            prefix[i] = prefix[i-1] * nums[i]
        
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]
        
        
        
        output[0] = postfix[1]
        output[-1] = prefix[-2]
        for i in range(1, len(nums) - 1, 1):
            output[i] = prefix[i-1] * postfix[i+1]
        return output
       

        


        