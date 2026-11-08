class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = Counter(nums)
        freq = [[] for i in range(len(nums)+1)]
        res = []
        for num,v in nums_map.items():
            freq[v].append(num)
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res