class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #right pass
        right = [0 for i in range(len(nums))]
        right[0] = nums[0]
        for i in range(1, len(nums), 1):
            right[i] = nums[i] * right[i-1]
        
        left = [0 for i in range(len(nums))]
        left[-1] = nums[-1]

        for i in range(len(nums) - 2,-1, -1):
            left[i] = nums[i] * left[i+1]
        
        ans = [0 for i in range(len(nums))]
        ans[0] = left[1]
        ans[-1] = right[-2]

        for i in range(1, len(nums)-1, 1):
            ans[i] = right[i-1] * left[i+1]
        return ans
        
