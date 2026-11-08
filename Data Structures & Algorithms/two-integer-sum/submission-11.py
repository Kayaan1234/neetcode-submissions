class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        res = []
        for index, number in enumerate(nums):
            to_find = target - number
            if to_find in nums_map:
                res = [nums_map.get(to_find), index]
                return res
            nums_map[number] = index
        