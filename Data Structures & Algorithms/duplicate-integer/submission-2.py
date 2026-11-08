class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = Counter(nums)
        print(map)
        for v in map.values():
            if v > 1:
                return True

        return False

        