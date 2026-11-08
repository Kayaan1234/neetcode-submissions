class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_chain = 0

        for num in num_set:
            if num-1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                max_chain = max(length, max_chain)
        return max_chain
            

