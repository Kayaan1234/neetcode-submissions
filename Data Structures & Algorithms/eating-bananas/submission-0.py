class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        res = high
        
    

        while low <= high:
            mid = (low+high) //2
            total = 0
            for pile in piles:
                total += math.ceil(pile/mid)
            if total <= h:
                res = min(res,mid)
                high = mid - 1
                
                
            else:
                low = mid + 1
        return res



