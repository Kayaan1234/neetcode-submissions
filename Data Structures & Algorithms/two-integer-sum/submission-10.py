class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        res = []
        for i, val in enumerate(nums):
            x = target - val
            if x in nums_map:
                res.append(nums_map.get(x))
                res.append(i)
                return res
            nums_map[val] = i
        return []
        


        

        