class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_chain = 0

        for num in num_set:
            # only start counting if num is the start of a sequence
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                max_chain = max(max_chain, length)

        return max_chain
            

