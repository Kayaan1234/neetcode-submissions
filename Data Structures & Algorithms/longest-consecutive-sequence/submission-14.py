class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        max_chain = 0
        for num in nums_set:
            if num -1 not in nums_set:
                chain = 1
                while num+chain in nums_set:
                    chain += 1
                max_chain = max(max_chain, chain)
        return max_chain