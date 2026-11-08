class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = Counter(nums)
        for v in nums_set.values():
            if v > 1:
                return True
        return False


        