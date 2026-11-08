class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            to_find = target - num
            if to_find in nums_map:
                return [nums_map.get(to_find), i]
            nums_map[num] = i
        
        