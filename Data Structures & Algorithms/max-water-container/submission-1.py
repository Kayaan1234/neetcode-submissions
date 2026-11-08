class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        width = r - l
        up = min(heights[l], heights[r])
        h = up * width
        while l < r:
            up = min(heights[l], heights[r])
            width = r - l
            

            
            if heights[l] >= heights[r]:
                r-=1
            elif heights[r] >= heights[l]:
                l+=1
            h = max(h, up * width)
        return h
