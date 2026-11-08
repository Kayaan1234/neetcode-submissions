class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)
        frequencies = count_nums.most_common(k)
        ans = []
        for i in range(len(frequencies)):
            ans.append(frequencies[i][0])

        return ans

        
        
            


  

        